# Demo

## Demo-1

In this demo we will see a basic example of creating an inventory file in `YAML` format.

```yaml
all:
  children:
    spine:
      hosts:
        DC1-SPINE1:
          ansible_host: 192.168.0.1
        DC1-SPINE2:
          ansible_host: 192.168.0.2
    leaf:
      children:
        rack01:
          hosts:
            DC1-LEAF1A:
              ansible_host: 192.168.0.3
            DC1-LEAF1B:
              ansible_host: 192.168.0.4
        rack02:
          hosts:
            DC1-LEAF2A:
              ansible_host: 192.168.0.5
            DC1-LEAF2B:
              ansible_host: 192.168.0.6
```

## Demo-2

Now we will represent the same inventory file in `INI` format.

```ini
[all:children]
spine
leaf

[spine]
DC1-SPINE1 ansible_host=192.168.0.1
DC1-SPINE2 ansible_host=192.168.0.2

[leaf:children]
rack01
rack02

[rack01]
DC1-LEAF1A ansible_host=192.168.0.3
DC1-LEAF1B ansible_host=192.168.0.4

[rack02]
DC1-LEAF2A ansible_host=192.168.0.5
DC1-LEAF2B ansible_host=192.168.0.6
```

## Demo-3

Using ansible-inventory we will print the inventory graph with the variables.

### Using YAML

```shell
% ansible-inventory -i inventory.yml --graph
@all:
  |--@leaf:
  |  |--@rack01:
  |  |  |--DC1-LEAF1A
  |  |  |--DC1-LEAF1B
  |  |--@rack02:
  |  |  |--DC1-LEAF2A
  |  |  |--DC1-LEAF2B
  |--@spine:
  |  |--DC1-SPINE1
  |  |--DC1-SPINE2
  |--@ungrouped:
```

### Using INI

```shell
% ansible-inventory -i inventory.ini --graph --vars
@all:
  |--@leaf:
  |  |--@rack01:
  |  |  |--DC1-LEAF1A
  |  |  |  |--{ansible_host = 192.168.0.3}
  |  |  |--DC1-LEAF1B
  |  |  |  |--{ansible_host = 192.168.0.4}
  |  |--@rack02:
  |  |  |--DC1-LEAF2A
  |  |  |  |--{ansible_host = 192.168.0.5}
  |  |  |--DC1-LEAF2B
  |  |  |  |--{ansible_host = 192.168.0.6}
  |--@spine:
  |  |--DC1-SPINE1
  |  |  |--{ansible_host = 192.168.0.1}
  |  |--DC1-SPINE2
  |  |  |--{ansible_host = 192.168.0.2}
  |--@ungrouped:
```

## Demo-4

Now we will specify the username & password which will be used to connect to the hosts.

Since the username & password `arista` is common to all devices we can add it at a level where its inherited by all hosts, instead of adding the value per host.

```yaml
---
  all:
    children:
      spine:
        hosts:
          DC1-SPINE1:
            ansible_host: 192.168.0.1
          DC1-SPINE2:
            ansible_host: 192.168.0.2
      leaf:
        children:
          rack01:
            hosts:
              DC1-LEAF1A:
                ansible_host: 192.168.0.3
              DC1-LEAF1B:
                ansible_host: 192.168.0.4
          rack02:
            hosts:
              DC1-LEAF2A:
                ansible_host: 192.168.0.5
              DC1-LEAF2B:
                ansible_host: 192.168.0.6
    vars:
      ansible_user: arista
      ansible_password: arista
```

Checking the vars

```shell
% ansible-inventory -i inventory.yml --graph --vars

@all:
  |--@leaf:
  |  |--@rack01:
  |  |  |--DC1-LEAF1A
  |  |  |  |--{ansible_host = 192.168.0.3}
  |  |  |  |--{ansible_password = arista}
  |  |  |  |--{ansible_user = arista}
  |  |  |--DC1-LEAF1B
  |  |  |  |--{ansible_host = 192.168.0.4}
  |  |  |  |--{ansible_password = arista}
  |  |  |  |--{ansible_user = arista}
  |  |--@rack02:
  |  |  |--DC1-LEAF2A
  |  |  |  |--{ansible_host = 192.168.0.5}
  |  |  |  |--{ansible_password = arista}
  |  |  |  |--{ansible_user = arista}
  |  |  |--DC1-LEAF2B
  |  |  |  |--{ansible_host = 192.168.0.6}
  |  |  |  |--{ansible_password = arista}
  |  |  |  |--{ansible_user = arista}
  |--@spine:
  |  |--DC1-SPINE1
  |  |  |--{ansible_host = 192.168.0.1}
  |  |  |--{ansible_password = arista}
  |  |  |--{ansible_user = arista}
  |  |--DC1-SPINE2
  |  |  |--{ansible_host = 192.168.0.2}
  |  |  |--{ansible_password = arista}
  |  |  |--{ansible_user = arista}
  |--@ungrouped:
  |--{ansible_password = arista}
  |--{ansible_user = arista}
```
