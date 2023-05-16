# Demo

The complete list of all modules is available [here](https://github.com/aristanetworks/ansible-cvp/#list-of-available-modules)

We will see examples of some of the commonly used modules.

## Demo-1

Get the device and container information from CVP using `arista.cvp.cv_facts_v3`

```yaml
---
- name: Demo-1 Playbook
  hosts: CloudVision
  connection: local
  gather_facts: no
  tasks:
    - name: Collect devices facts from {{ inventory_hostname }}
      arista.cvp.cv_facts_v3:
        facts:
          - configlets
          - devices
          - containers
      register: cvp_facts
    
    - name: Print CVP Facts
      ansible.builtin.debug:
        msg: "{{ cvp_facts }}"
```

## Demo-2

In this Demo we will generate the EOS MLAG configuration using Jinja2 rendering.

```yaml
- name: Generate EOS MLAG Configuration
  hosts: rack01
  gather_facts: false
  tasks:
    - name: Create backup folder
      ansible.builtin.file:
        path: "{{ playbook_dir }}/backups"
        state: directory
        mode: '0755'
      run_once: true
    
    - name: Create configuration folder
      ansible.builtin.file:
        path: "{{ playbook_dir }}/intended/configs"
        state: directory
        mode: '0755'
      run_once: true
    
    - name: Backup existing Configuration
      arista.eos.eos_facts:
        gather_subset:
          - config
    
    - name: Backup configuration to file
      ansible.builtin.copy:
        content: "{{ ansible_facts.net_config }}"
        dest: "{{ playbook_dir }}/backups/{{ inventory_hostname }}_backup.cfg"
      delegate_to: localhost
    
    - name: Render MLAG configuration
      ansible.builtin.template:
        src: "{{ playbook_dir }}/eos-mlag.j2"
        dest: "{{ playbook_dir }}/intended/configs/{{ inventory_hostname }}.cfg"
```

Then use this generated MLAG configuration we will upload as configlets to CVP. And assign it to the leaf1, leaf2 switches and execute the generated tasks.

```yaml
- name: Demo ansible-cvp
  hosts: CloudVision
  connection: local
  gather_facts: false
  vars:
    configlet_list:
      DC1_Leaf1_MLAG: "{{ lookup( 'file', playbook_dir + '/intended/configs/leaf1.cfg' ) }}"
      DC1_Leaf2_MLAG: "{{ lookup( 'file', playbook_dir + '/intended/configs/leaf2.cfg' ) }}"
    device_list:
      - fqdn: "leaf2.atd.lab"
        parentContainerName: "Leaf"
        configlets:
          - "ATD-INFRA"
          - "BaseIPv4_Leaf2"
          - "DC1_Leaf2_MLAG"
      - fqdn: "leaf1.atd.lab"
        parentContainerName: "Leaf"
        configlets:
          - "ATD-INFRA"
          - "BaseIPv4_Leaf1"
          - "DC1_Leaf1_MLAG"
  tasks:
    - name: Create configlets on CVP
      arista.cvp.cv_configlet_v3:
        configlets: "{{ configlet_list }}"
        configlets_notes: "Configlets managed by Ansible"
        state: present
      register: cvp_configlet
    - name: Map Configlets to devices
      arista.cvp.cv_device_v3:
        devices: "{{ device_list }}"
        state: present
        search_key: fqdn
      register: cvp_device
    - name: Execute resulting tasks from previous operation
      arista.cvp.cv_task_v3:
        tasks: "{{ cvp_device.taskIds }}"
      register: cvp_task
      failed_when: not cvp_task.success
```
