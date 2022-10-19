# Jinja Lab

In this folder your skills will be tested on what you have learned about JINJA.

From the `Programmability IDE` perform the following operations.

## Challenge-1

- Using the following YAML as input

```yaml
---
radius_servers:
  - host: 192.168.0.1
    key: 0207165218120E
  - host: 192.168.1.1
    key: 0107165218120F
aaa_server_groups:
  - name: atds
    type: radius
    servers:
      - server: 192.168.0.1
      - server: 192.168.1.1
aaa_authentication:
  login:
    default: group atds local
  policies:
    local:
      allow_nopassword: true
aaa_authorization:
  exec:
    default: group atds local
  commands:
    all_default: local

```

- Build a JINJA2 template to generate the following CLI output:

```shell
!
radius-server host 192.168.0.1 key 7 0207165218120E
radius-server host 192.168.1.1 key 7 0107165218120F
!
aaa group server radius atds
   server 192.168.0.1
   server 192.168.1.1
!
aaa authentication login default group atds local
aaa authentication policy local allow-nopassword-remote-login
aaa authorization exec default group atds local
aaa authorization commands all default local
!
```

## Challenge-2

- Using EAPI obtain the following information from all switches except `cvx01`
  - Hostname
  - MAC Address
  - LLDP Neighbors

- Store the above in an appropriate python data structure
- Create a JINJA template and using the above data structure generate the following output

```shell
Total of 8 devices listed
----------------------------------------------

leaf1 ( System MAC Address 00:1c:73:b2:d5:01 )
  Total of 5 Neighbor Devices found in LLDP Table
    - leaf1 [ Ethernet1 ] <----> [ Ethernet1 ] leaf2 
    - leaf1 [ Ethernet2 ] <----> [ Ethernet2 ] spine1 
    - leaf1 [ Ethernet3 ] <----> [ Ethernet2 ] spine2 
    - leaf1 [ Ethernet4 ] <----> [ Ethernet1 ] host1 
    - leaf1 [ Ethernet6 ] <----> [ Ethernet6 ] leaf2 

leaf2 ( System MAC Address 00:1c:73:b3:d5:01 )
  Total of 5 Neighbor Devices found in LLDP Table
    - leaf2 [ Ethernet1 ] <----> [ Ethernet1 ] leaf1 
    - leaf2 [ Ethernet2 ] <----> [ Ethernet3 ] spine1 
    - leaf2 [ Ethernet3 ] <----> [ Ethernet3 ] spine2 
    - leaf2 [ Ethernet4 ] <----> [ Ethernet2 ] host1 
    - leaf2 [ Ethernet6 ] <----> [ Ethernet6 ] leaf1 

leaf3 ( System MAC Address 00:1c:73:b4:d5:01 )
  Total of 5 Neighbor Devices found in LLDP Table
    - leaf3 [ Ethernet1 ] <----> [ Ethernet1 ] leaf4 
    - leaf3 [ Ethernet2 ] <----> [ Ethernet4 ] spine1 
    - leaf3 [ Ethernet3 ] <----> [ Ethernet4 ] spine2 
    - leaf3 [ Ethernet4 ] <----> [ Ethernet1 ] host2 
    - leaf3 [ Ethernet6 ] <----> [ Ethernet6 ] leaf4 

leaf4 ( System MAC Address 00:1c:73:b5:d5:01 )
  Total of 6 Neighbor Devices found in LLDP Table
    - leaf4 [ Ethernet1 ] <----> [ Ethernet1 ] leaf3 
    - leaf4 [ Ethernet2 ] <----> [ Ethernet5 ] spine1 
    - leaf4 [ Ethernet3 ] <----> [ Ethernet5 ] spine2 
    - leaf4 [ Ethernet4 ] <----> [ Ethernet2 ] host2 
    - leaf4 [ Ethernet5 ] <----> [ Ethernet4 ] host2 
    - leaf4 [ Ethernet6 ] <----> [ Ethernet6 ] leaf3 

spine1 ( System MAC Address 00:1c:73:b0:d5:01 )
  Total of 6 Neighbor Devices found in LLDP Table
    - spine1 [ Ethernet1 ] <----> [ Ethernet1 ] spine2 
    - spine1 [ Ethernet2 ] <----> [ Ethernet2 ] leaf1 
    - spine1 [ Ethernet3 ] <----> [ Ethernet2 ] leaf2 
    - spine1 [ Ethernet4 ] <----> [ Ethernet2 ] leaf3 
    - spine1 [ Ethernet5 ] <----> [ Ethernet2 ] leaf4 
    - spine1 [ Ethernet6 ] <----> [ Ethernet6 ] spine2 

spine2 ( System MAC Address 00:1c:73:b1:d5:01 )
  Total of 6 Neighbor Devices found in LLDP Table
    - spine2 [ Ethernet1 ] <----> [ Ethernet1 ] spine1 
    - spine2 [ Ethernet2 ] <----> [ Ethernet3 ] leaf1 
    - spine2 [ Ethernet3 ] <----> [ Ethernet3 ] leaf2 
    - spine2 [ Ethernet4 ] <----> [ Ethernet3 ] leaf3 
    - spine2 [ Ethernet5 ] <----> [ Ethernet3 ] leaf4 
    - spine2 [ Ethernet6 ] <----> [ Ethernet6 ] spine1 

host1 ( System MAC Address 00:1c:73:b6:d5:01 )
  Total of 2 Neighbor Devices found in LLDP Table
    - host1 [ Ethernet1 ] <----> [ Ethernet4 ] leaf1 
    - host1 [ Ethernet2 ] <----> [ Ethernet4 ] leaf2 

host2 ( System MAC Address 00:1c:73:b7:d5:01 )
  Total of 3 Neighbor Devices found in LLDP Table
    - host2 [ Ethernet1 ] <----> [ Ethernet4 ] leaf3 
    - host2 [ Ethernet2 ] <----> [ Ethernet4 ] leaf4 
    - host2 [ Ethernet4 ] <----> [ Ethernet5 ] leaf4
```

## Challenge-3

- Open `Console Access` from your ATD Lab GUI.
- From the main menu select the option number `1.Reset All Devices to Base ATD (reset)`
- Wait for the lab deployment to complete

```shell
*****************************************
*****Jump Host for Arista Test Drive*****
*****************************************


==========Main Menu==========

Please select from the following options: 
1. Reset All Devices to Base ATD (reset)
2. MLAG Lab (mlag)
3. BGP Lab (bgp)
4. VXLAN Lab (vxlan) excludes leaf3 instead of leaf4
5. EVPN Type 2 Lab (l2evpn) excludes leaf3 instead of leaf4
6. EVPN Type 5 Lab (l3evpn) excludes leaf3 instead of leaf4
7. CVP lab (cvp)
8. CVP lab for Studios L3LS/EVPN (cvpstudl3lsevpn)


97. Additional Labs (labs)
98. SSH to Devices (ssh)
99. Exit LabVM (quit/exit) - CTRL + c

What would you like to do?: 1
Starting deployment for Datacenter - reset lab...
Gathering task information...
Waiting on change control to finish executing...
Running additional setup commands...
Lab Setup Completed. Please press Enter to continue...
```

- Once completed head back to `Programmability IDE`
- Here using a YAML and JINJA script to generate the following MLAG configuration for:
  - leaf1 & leaf2
  - leaf3 & leaf4

### leaf1

```shell
!
vlan 4094
   trunk group MLAGPEER
!
interface Vlan4094
   description MLAG PEER LINK
   ip address 172.16.12.1/30
!
no spanning-tree vlan-id 4094
!
interface Port-Channel10
   description MLAG PEER LINK - LEAF2
   switchport mode trunk
   switchport trunk group MLAGPEER
!
interface Ethernet1
   description MLAG PEER LINK - LEAF2
   switchport mode trunk
   channel-group 10 mode active
!
interface Ethernet6
   description MLAG PEER LINK - LEAF2
   switchport mode trunk
   channel-group 10 mode active
!
mlag configuration
   domain-id MLAG12
   local-interface Vlan4094
   peer-address 172.16.12.2
   peer-link Port-Channel10
!
```

### leaf2

```shell
!
vlan 4094
   trunk group MLAGPEER
!
interface Vlan4094
   description MLAG PEER LINK
   ip address 172.16.12.2/30
!
no spanning-tree vlan-id 4094
!
interface Port-Channel10
   description MLAG PEER LINK - LEAF1
   switchport mode trunk
   switchport trunk group MLAGPEER
!
interface Ethernet1
   description MLAG PEER LINK - LEAF1
   switchport mode trunk
   channel-group 10 mode active
!
interface Ethernet6
   description MLAG PEER LINK - LEAF1
   switchport mode trunk
   channel-group 10 mode active
!
mlag configuration
   domain-id MLAG12
   local-interface Vlan4094
   peer-address 172.16.12.1
   peer-link Port-Channel10
!
```

### leaf3

```shell
!
vlan 4094
   trunk group MLAGPEER
!
interface Vlan4094
   description MLAG PEER LINK
   ip address 172.16.34.1/30
!
no spanning-tree vlan-id 4094
!
interface Port-Channel10
   description MLAG PEER LINK - LEAF4
   switchport mode trunk
   switchport trunk group MLAGPEER
!
interface Ethernet1
   description MLAG PEER LINK - LEAF4
   switchport mode trunk
   channel-group 10 mode active
!
interface Ethernet6
   description MLAG PEER LINK - LEAF4
   switchport mode trunk
   channel-group 10 mode active
!
mlag configuration
   domain-id MLAG34
   local-interface Vlan4094
   peer-address 172.16.34.2
   peer-link Port-Channel10
!
```

### leaf4

```shell
!
vlan 4094
   trunk group MLAGPEER
!
interface Vlan4094
   description MLAG PEER LINK
   ip address 172.16.34.2/30
!
no spanning-tree vlan-id 4094
!
interface Port-Channel10
   description MLAG PEER LINK - LEAF3
   switchport mode trunk
   switchport trunk group MLAGPEER
!
interface Ethernet1
   description MLAG PEER LINK - LEAF3
   switchport mode trunk
   channel-group 10 mode active
!
interface Ethernet6
   description MLAG PEER LINK - LEAF3
   switchport mode trunk
   channel-group 10 mode active
!
mlag configuration
   domain-id MLAG34
   local-interface Vlan4094
   peer-address 172.16.34.1
   peer-link Port-Channel10
!
```

## Challenge-4

- Upload the generated configuration in `Challenge-3` to CVP as configlets:
  - Phase-1-MLAG-leaf1
  - Phase-1-MLAG-leaf2
  - Phase-1-MLAG-leaf3
  - Phase-1-MLAG-leaf4

- Assign the configlets to the respective devices
- Execute the generated tasks via a change control on CVP
- Using EAPI confirm the MLAG State of all leaf switches.
