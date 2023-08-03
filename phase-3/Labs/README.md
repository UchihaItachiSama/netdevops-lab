# Labs

- Prerequisite
  - Complete the Phase-1 training and Labs
  - Complete the Phase-2 training and Labs.
  - Spin up a `Dual Datacenter` ATD lab
  - If ATD access is not there spin up a cEOS/vEOS lab with 2 Spine + 4 Leaf + 2 switches as hosts. Similar to topology [here](`../Demo/images/demo-1.png`).

## Lab 1

- For DC1 in the dual datacenter topology, create and deploy Single DC L3LS EVPN/VxLAN Asymmetric IRB with eBGP overlay and OSPF underlay.
- Use host files present in lab folder.

## Lab 2

- For DC2 in the dual datacenter topology, create and deploy a single DC L3LS EVPN/VxLAN Symmetric IRB with eBGP overlay and eBGP underlay.
- Use host files present in lab folder.

All hosts in their respective local DCs should be able to ping each other at end of deployment.
