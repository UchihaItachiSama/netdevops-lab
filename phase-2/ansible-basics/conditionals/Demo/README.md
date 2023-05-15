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

## Demo-3

Here `block` keyword is used to group together two tasks that configure two uplinks on a leaf switch. If either one of them fails, the `rescue` keyword is used to execute a task that rolls back the configuration to the state prior to uplink configurations. The `always` keyword is used to ensure that a task is run to show the interface configuration at the end of the play whether the tasks are successful or not.

```yaml
---
- name: Demo-3 Playbook
  hosts: leaf1
  gather_facts: false
  tasks:
    - name: Configure L3 interface
      block:
        - name: Create configuration checkpoint
          arista.eos.eos_command:
            commands: configure checkpoint save ckp-demo-3-1 

        - name: Set interface Ethernet2 configuration
          arista.eos.eos_config:
            lines:
              - description UPLINK TO SPINE1
              - ip address 10.10.0.1/30
            parents: interface Ethernet2
        
        - name: Set interface Ethernet3 configuration
          arista.eos.eos_config:
            lines:
              - description UPLINK TO SPINE2
              - ip address 10.10.0.255/30    <<-- rigged to fail
            parents: interface Ethernet3
      
      rescue:
        - name: Roll back from checkpoint
          arista.eos.eos_command:
            commands: configure checkpoint restore ckp-demo-3-1
      
      always:
        - name: Check interface configuration
          arista.eos.eos_command:
            commands: show running-config interfaces Ethernet 2-3
          register: output
        
        - name: Print output
          ansible.builtin.debug:
            msg: "{{ output.stdout_lines }}"
 ```           
