# EAPI Lab

In this folder your skills will be tested on what you have learned about EPI.

From the `Programmability IDE` perform the following operations.

## Challenge-1

- Using a python script collect and print the following information for all switches except `cvx01` in the topology:
  - Hostname
  - Model
  - Software Version
  - TerminAttr version
  - System MAC Address

## Challenge-2

- Open `Console Access` from your ATD Lab GUI.
- From the main menu select the option number `2. MLAG Lab (mlag)`
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

What would you like to do?: 2
Starting deployment for Datacenter - mlag lab...
Gathering task information...
Waiting on change control to finish executing...
Lab Setup Completed. Please press Enter to continue...
```

- Once completed head back to `Programmability IDE`
- Here create a python script to get and print the `Hostname` & `MLAG State` for all devices except `cvx01`
- If MLAG State is `active` print the MLAG Interfaces output as seen on CLI i.e `text` output.

## Challenge-3

- From `Challenge-2` we can see MLAG is down between `leaf3` and `leaf4`
- Obtain and print the following information from `leaf3` and `leaf4`
  - MLAG configuration
- From above you can see MLAG configuration is missing from `leaf4`

## Challenge-4

- This will be a long one so get ready.
- We will configure `leaf4` with the MLAG configuration and bring up MLAG between `leaf3` and `leaf4`
- Configure the MLAG VLAN (both Layer 2 and Layer 3)

```shell
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
```

- Configure the port-channel

```shell
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
```

- Define the MLAG DOMAIN

```shell
!
mlag
  domain-id MLAG34
  local-interface vlan 4094
  peer-address 172.16.34.1
  peer-link port-channel 10
!
```

- Configure Port-channels and interfaces on Leaf4 connecting to Spine1 & Spine2

```shell
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
```

- Configure Port-channels on Leaf4 connecting to Host2

```shell
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
```

- Verify the MLAG State now on all switches (except `cvx01`) and check the MLAG Interfaces (hint: you can reuse script from Challenge-2)

## Challenge-5

- Run ping from `Host1` to `Host2` via ping from EAPI

```shell
From host1

ping 172.16.112.202 repeat 10
```
