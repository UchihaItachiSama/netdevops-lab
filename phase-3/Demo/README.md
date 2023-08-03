# Demo

## Demo 1 - Single DC L3LS EVPN/VXLAN Symmetric IRB (eBGP overlay & eBGP underlay) deployment with eAPI

### Topology

<img src="images/demo-1.png" height="300">

### Deploying

1. Apply the following configurations to `s1-host1` and `s1-host2` either using CLI or CVP.

```shell
host_configlets
├──  AVD_L3LS-s1-host1.cfg
└──  AVD_L3LS-s1-host2.cfg
```

2. Run the following playbook to generate and deploy the configuration

```shell
$ ansible-playbook playbooks/fabric-deploy.yml
```

3. Login to the end host devices and run end-to-end pings

```shell
s1-host1#ping vrf SERVER_A  10.10.21.10
PING 10.10.21.10 (10.10.21.10) 72(100) bytes of data.
80 bytes from 10.10.21.10: icmp_seq=1 ttl=62 time=9.81 ms
80 bytes from 10.10.21.10: icmp_seq=2 ttl=62 time=5.18 ms
80 bytes from 10.10.21.10: icmp_seq=3 ttl=62 time=5.26 ms
80 bytes from 10.10.21.10: icmp_seq=4 ttl=62 time=5.41 ms
80 bytes from 10.10.21.10: icmp_seq=5 ttl=62 time=5.09 ms

--- 10.10.21.10 ping statistics ---
5 packets transmitted, 5 received, 0% packet loss, time 36ms
rtt min/avg/max/mdev = 5.090/6.154/9.817/1.834 ms, ipg/ewma 9.001/7.921 ms

s1-host1#ping vrf SERVER_A  10.10.22.10
PING 10.10.22.10 (10.10.22.10) 72(100) bytes of data.
80 bytes from 10.10.22.10: icmp_seq=1 ttl=62 time=8.94 ms
80 bytes from 10.10.22.10: icmp_seq=2 ttl=62 time=4.99 ms
80 bytes from 10.10.22.10: icmp_seq=3 ttl=62 time=5.15 ms
80 bytes from 10.10.22.10: icmp_seq=4 ttl=62 time=5.15 ms
80 bytes from 10.10.22.10: icmp_seq=5 ttl=62 time=4.64 ms

--- 10.10.22.10 ping statistics ---
5 packets transmitted, 5 received, 0% packet loss, time 33ms
rtt min/avg/max/mdev = 4.641/5.778/8.941/1.593 ms, ipg/ewma 8.270/7.297 ms


s1-host1#ping vrf SERVER_A  10.10.12.10
PING 10.10.12.10 (10.10.12.10) 72(100) bytes of data.
80 bytes from 10.10.12.10: icmp_seq=1 ttl=63 time=3.63 ms
80 bytes from 10.10.12.10: icmp_seq=2 ttl=63 time=2.47 ms
80 bytes from 10.10.12.10: icmp_seq=3 ttl=63 time=2.61 ms
80 bytes from 10.10.12.10: icmp_seq=4 ttl=63 time=2.39 ms
80 bytes from 10.10.12.10: icmp_seq=5 ttl=63 time=2.35 ms

--- 10.10.12.10 ping statistics ---
5 packets transmitted, 5 received, 0% packet loss, time 13ms
rtt min/avg/max/mdev = 2.357/2.696/3.635/0.480 ms, ipg/ewma 3.251/3.145 ms
```

4. Check the BGP routes and states from VTEPs

## Demo 2 - Single DC L3LS EVPN/VXLAN Symmetric IRB (iBGP overlay & OSPF underlay) deployment with CVP

### Deploying

1. Apply the following configurations to `s2-host1` and `s2-host2` either using CLI or CVP.

```shell
host_configlets
├──  AVD_L3LS-s2-host1.cfg
└──  AVD_L3LS-s2-host2.cfg
```

2.a. Run the following playbook to generate the configuration

```shell
$ ansible-playbook playbooks/fabric-build.yml
```

2.b. Run the following playbook to deploy the generated configuration via CVP

```shell
$ ansible-playbook playbooks/fabric-deploy-CVP.yml
```

2.c Login to CVP and execute the generated Tasks using a Change Control.

3. Login to the end host devices and run end-to-end pings

```shell
s2-host1#ping vrf SERVER_A 10.10.12.20
PING 10.10.12.20 (10.10.12.20) 72(100) bytes of data.
80 bytes from 10.10.12.20: icmp_seq=1 ttl=63 time=4.31 ms
80 bytes from 10.10.12.20: icmp_seq=2 ttl=63 time=2.44 ms
80 bytes from 10.10.12.20: icmp_seq=3 ttl=63 time=2.42 ms
80 bytes from 10.10.12.20: icmp_seq=4 ttl=63 time=2.46 ms
80 bytes from 10.10.12.20: icmp_seq=5 ttl=63 time=2.45 ms

--- 10.10.12.20 ping statistics ---
5 packets transmitted, 5 received, 0% packet loss, time 16ms
rtt min/avg/max/mdev = 2.424/2.820/4.313/0.747 ms, ipg/ewma 4.105/3.541 ms

s2-host1#ping vrf SERVER_A 10.10.21.20
PING 10.10.21.20 (10.10.21.20) 72(100) bytes of data.
80 bytes from 10.10.21.20: icmp_seq=1 ttl=62 time=6.49 ms
80 bytes from 10.10.21.20: icmp_seq=2 ttl=62 time=4.34 ms
80 bytes from 10.10.21.20: icmp_seq=3 ttl=62 time=4.45 ms
80 bytes from 10.10.21.20: icmp_seq=4 ttl=62 time=4.32 ms
80 bytes from 10.10.21.20: icmp_seq=5 ttl=62 time=4.58 ms

--- 10.10.21.20 ping statistics ---
5 packets transmitted, 5 received, 0% packet loss, time 24ms
rtt min/avg/max/mdev = 4.325/4.842/6.497/0.835 ms, ipg/ewma 6.153/5.645 ms

s2-host1#ping vrf SERVER_A 10.10.22.20
PING 10.10.22.20 (10.10.22.20) 72(100) bytes of data.
80 bytes from 10.10.22.20: icmp_seq=1 ttl=62 time=6.29 ms
80 bytes from 10.10.22.20: icmp_seq=2 ttl=62 time=5.15 ms
80 bytes from 10.10.22.20: icmp_seq=3 ttl=62 time=4.67 ms
80 bytes from 10.10.22.20: icmp_seq=4 ttl=62 time=4.65 ms
80 bytes from 10.10.22.20: icmp_seq=5 ttl=62 time=6.92 ms

--- 10.10.22.20 ping statistics ---
5 packets transmitted, 5 received, 0% packet loss, time 24ms
rtt min/avg/max/mdev = 4.658/5.541/6.926/0.913 ms, ipg/ewma 6.105/5.941 ms
```

4. Check the BGP routes and states from VTEPs
