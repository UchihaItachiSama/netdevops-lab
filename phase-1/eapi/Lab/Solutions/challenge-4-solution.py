#!/usr/bin/python3

from pprint import pprint as pp
from jsonrpclib import Server
import ssl
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context

DEVICE_IPS = [
    'leaf4', 
]

MLAG_VLAN = """
!
vlan 4094
  trunk group MLAGPEER
!
no spanning-tree vlan-id 4094
!
interface Vlan4094
  description MLAG PEER LINK
  ip address 172.16.34.2/30
!
"""

PEER_LAG = """
!
interface port-channel 10
  description MLAG PEER LINK - LEAF3
  switchport mode trunk
  switchport trunk group MLAGPEER
!
interface ethernet 1,6
  description MLAG PEER LINK - LEAF3
  channel-group 10 mode active
!
"""

MLAG_DOMAIN = """
!
mlag
  domain-id MLAG34
  local-interface vlan 4094
  peer-address 172.16.34.1
  peer-link port-channel 10
!
"""

SPINE_LAG = """
!
interface port-channel 34
  description MLAG - SPINE 1 & 2
  switchport mode trunk
  mlag 34
!
interface ethernet 2
  description SPINE1
  channel-group 34 mode active
!
interface ethernet 3
  description SPINE2
  channel-group 34 mode active
!
"""

HOST_LAG = """
!
interface port-channel 4
  description MLAG - HOST2
  switchport access vlan 12
  mlag 4
!
interface ethernet 4
  description HOST2
  channel-group 4 mode active
!
interface ethernet 5
  shutdown
!
"""

def checkMLAGConfig(switch):
    # Check MLAG configuration
    result = switch.runCmds('latest', ['show running-config section mlag'], 'text')[0]
    mlag_config = result['output']
    print("Switch '{}' has following MLAG Configuration: \n{}\n".format(
        device,
        mlag_config
    ))

# Update the credentials based on your Lab Setup
USERNAME = 'arista'
PASSWORD = 'arista'

if __name__ == '__main__':
    for device in DEVICE_IPS:
        switch = Server( "https://{}:{}@{}/command-api".format(
            USERNAME,
            PASSWORD,
            device
        ) )
        # Check MLAG configuration
        checkMLAGConfig(switch)

        # Add MLAG Configuration
        MLAG_CONFIGS = [
            MLAG_VLAN,
            PEER_LAG,
            MLAG_DOMAIN,
            SPINE_LAG,
            HOST_LAG
        ]
        print("\n\n Configuring MLAG on leaf4\n\n")
        for config in MLAG_CONFIGS:
            cmdList = ['enable', 'configure terminal']
            cmdList.extend(config.split("\n"))
            cmdList.append('end')
            result = switch.runCmds('latest', cmdList, "json")
        print("\n\n MLAG Configuration completed on leaf4\n\n")
        
        # Check MLAG configuration
        checkMLAGConfig(switch)