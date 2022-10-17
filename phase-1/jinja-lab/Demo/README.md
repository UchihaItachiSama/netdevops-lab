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
