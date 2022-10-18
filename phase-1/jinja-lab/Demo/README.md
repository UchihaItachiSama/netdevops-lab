# Demo

## Demo-1

- In this demo we will take a look at a very basic example of jinja2 template.
- We will geneate the following CLI configuration:

```shell
!
hostname leaf1
!
ntp server 192.168.0.1
!
spanning-tree mode mstp
!
service routing protocols model multi-agent
!
```

- We will see demo using two type of inputs

### YAML

```yaml
---
hostname: leaf1
ntp:
  server: 192.168.0.1
spanning_tree:
  mode: mstp
service_routing_protocols_model: multi-agent
```

### JSON

```json
{
    "hostname": "leaf1",
    "ntp": {
        "server": "192.168.0.1"
    },
    "spanning_tree": {
        "mode": "mstp"
    },
    "service_routing_protocols_model": "multi-agent"
}
```

- Run the `demo-1.py` script

```shell
python3 demo-1.py
```

## Demo-2

- In this demo we will take a look at For Loops in Jinja templates.
- We will render the following CLI output

```shell
!
interface Ethernet2
   description LEAF1
   no switchport
   ip address 10.101.201.201/24
!
interface Ethernet3
   description LEAF2
   no switchport
   ip address 10.102.201.201/24
!
interface Ethernet4
   description LEAF3
   no switchport
   ip address 10.103.201.201/24
!
interface Ethernet5
   description LEAF4
   no switchport
   ip address 10.104.201.201/24
!
```

- We will see demo using two type of inputs

### YAML

```yaml
ethernet_interfaces:
  Ethernet2:
    description: LEAF1
    type: 'no switchport'
    ip_address: 10.101.201.201/24
  Ethernet3:
    description: LEAF2
    type: 'no switchport'
    ip_address: 10.102.201.201/24
  Ethernet4:
    description: LEAF3
    type: 'no switchport'
    ip_address: 10.103.201.201/24
  Ethernet5:
    description: LEAF4
    type: 'no switchport'
    ip_address: 10.104.201.201/24
```

### JSON

```json
{
    "ethernet_interfaces": {
        "Ethernet2": {
            "description": "LEAF1",
            "type": "no switchport",
            "ip_address": "10.101.201.201/24"
        },
        "Ethernet3": {
            "description": "LEAF2",
            "type": "no switchport",
            "ip_address": "10.102.201.201/24"
        },
        "Ethernet4": {
            "description": "LEAF3",
            "type": "no switchport",
            "ip_address": "10.103.201.201/24"
        },
        "Ethernet5": {
            "description": "LEAF4",
            "type": "no switchport",
            "ip_address": "10.104.201.201/24"
        }
    }
}
```

- Run the `demo-2.py` script

```shell
python3 demo-2.py
```

# Demo-3

- In this demo we will take a look at if/else in Jinja template
- We will render the following output

```shell
!
management api http-commands
   protocol http
   protocol unix-socket
   no shutdown
   !
   vrf MGMT
      no shutdown
   !
   vrf default
      no shutdown
!
```

- We will see demo using two type of inputs

### YAML

```yaml
---
management_api_http:
  enable_http: false
  enable_https: true
  enable_unix_socket: true
  enable_vrfs:
    - default
    - MGMT
```

### JSON

```json
{
    "management_api_http": {
        "enable_http": false,
        "enable_https": true,
        "enable_unix_socket": true,
        "enable_vrfs": [
          "default",
          "MGMT"
        ]
    }
}
```

- Run the `demo-3.py` script

```shell
python3 demo-3.py
```
