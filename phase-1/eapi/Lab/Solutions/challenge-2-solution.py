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
    'leaf1',
    'leaf2',
    'leaf3', 
    'leaf4', 
    'spine1', 
    'spine2', 
    'host1', 
    'host2'
]

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
        result = switch.runCmds('latest', ['show hostname', 'show mlag'])
        hostname = result[0]['hostname']
        mlag = result[1]
        print('Hostname: {} | MLAG State: {}\n'.format(
            hostname,
            mlag['state']
        ))
        if mlag['state'] == 'active':
            result = switch.runCmds('latest', ['show mlag interfaces'], 'text')
            print(result[0]['output'])