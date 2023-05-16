# Demo

## Demo-0

Basic example of `loop` to iterate over a list of interfaces and configure them using `arista.eos.eos_interfaces` module

```yaml
---
- name: Demo-0 Playbook
  hosts: spines
  gather_facts: false
  tasks:
    - name: Configure Interfaces
      arista.eos.eos_interfaces:
        config:
          - name: "{{ item.name }}"
            description: Configured using Ansible
            mode: layer3
            enabled: true
            mtu: 9000
      loop:
        - Ethernet2
        - Ethernet3
        - Ethernet4
        - Ethernet5
```

## Demo-1

We use the `arista.eos.eos_interfaces` module to configure interfaces on the spines. the `loop` directive specifies the list of hashes. During execution, Ansible will iterate over each item in the list and configure an interface with the specified name and description.

```yaml
---
- name: Demo-1 Playbook
  hosts: spines
  gather_facts: false
  tasks:
    - name: Configure Interfaces
      arista.eos.eos_interfaces:
        config:
          - name: "{{ item.name }}"
            description: "{{ item.description }}"
            mode: layer3
            enabled: true
            mtu: 9000
      loop:
        - { name: 'Ethernet2', description: 'P2P_LINK_TO_LEAF1' }
        - { name: 'Ethernet3', description: 'P2P_LINK_TO_LEAF2' }
        - { name: 'Ethernet4', description: 'P2P_LINK_TO_LEAF3' }
        - { name: 'Ethernet5', description: 'P2P_LINK_TO_LEAF4' }
```

## Demo-2

Here we will see the same example as `Demo-1` but using a dictionary of interface attributes.

> Note that the dict2items filter is used to convert the dictionary into a list of key-value pairs. This allows Ansible to iterate over each item in the list using the loop directive.

```yaml
---
- name: Demo-1 Playbook
  hosts: spines
  gather_facts: false
  vars:
    spine_interfaces:
      Ethernet2:
        description: P2P_LINK_TO_LEAF1
      Ethernet3:
        description: P2P_LINK_TO_LEAF2
      Ethernet4:
        description: P2P_LINK_TO_LEAF3
      Ethernet5:
        description: P2P_LINK_TO_LEAF4
  tasks:
    - name: Configure Interfaces
      arista.eos.eos_interfaces:
        config:
          - name: "{{ item.key }}"
            description: "{{ item.value.description }}"
            mode: layer3
            enabled: true
            mtu: 9000
      loop: "{{ spine_interfaces | dict2items }}"
```
