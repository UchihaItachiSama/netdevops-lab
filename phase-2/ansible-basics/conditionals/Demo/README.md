# Demo

## Demo-1

Using the basic `when` conditional, check if VLAN configuration is already present on the switch, before creating it.

```yaml
---
- name: Demo-1 Playbook
  hosts: leafs
  gather_facts: false
  vars:
    vlan_id: "10"
    vlan_name: Storage_Vlan
  tasks:
    - name: Get vlan information from Switch
      arista.eos.eos_command:
        commands:
          - command: show vlan
            output: json
      register: vlans_output
    
    - name: Print vlan information
      ansible.builtin.debug:
        msg: "{{ vlans_output.stdout_lines[0].vlans.keys() }}"

    - name: Create vlan
      arista.eos.eos_config:
        lines:
          - vlan {{ vlan_id }}
          - name {{ vlan_name }}
        parents: vlan {{ vlan_id }}
      when: vlan_id not in vlans_output.stdout_lines[0].vlans.keys()
```

## Demo-2

In this example, the `until` conditional is used to check if the route exists for `192.168.12.0/24` subnet. If the route is not found the task will be retried up to 50 times with a delay of 2 seconds.

```yaml
---
- name: Wait for L3 interfaces to be configured
  hosts: rack01
  gather_facts: false
  tasks:
    - name: Check route
      arista.eos.eos_command:
        commands:
          - command: show ip route 192.168.12.0/24
            output: json
      register: output
      until: output.stdout_lines[0].vrfs.default.routes.keys() | length > 0
      delay: 2
      retries: 50
```
