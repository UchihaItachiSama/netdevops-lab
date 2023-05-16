# Demo

The complete list of all modules is available [here](https://github.com/ansible-collections/arista.eos#modules)

We will see examples of some of the commonly used modules.

## Demo-1

Using `arista.eos.eos_facts` collect facts from Arista devices running the EOS operating system.

```yaml
- name: Demo-1 Playbook
  hosts: spine1
  gather_facts: false
  tasks:
    - name: Gather EOS Facts
      arista.eos.eos_facts:
        gather_subset:
          - config
    - name: Print EOS Facts
      ansible.builtin.debug:
        msg: "{{ ansible_facts.net_config }}"
```

## Demo-2

Using `arista.eos.eos_command` we can send arbitrary set of commands to an EOS node and get the result.

```yaml
---
- name: Demo-2 Playbook
  hosts: all
  gather_facts: false
  tasks:
    - name: Run commands
      arista.eos.eos_command:
        commands:
          - command: show interfaces status connected
            output: text
          - command: show arp
            output: json
      register: cmd_output
    - name: Print command output
      ansible.builtin.debug:
        msg: "{{ cmd_output.stdout_lines }}"
```

## Demo-3

Using `arista.eos.eos_config` we will configure MLAG on leaf1, leaf2 switches.

```yaml
---
- name: Demo-3 Play
  hosts: rack01
  gather_facts: false
  tasks:
    - name: Configure MLAG on leaf switches {{ ansible_play_hosts }}
      arista.eos.eos_config:
        src: "{{ playbook_dir }}/eos-mlag.j2"
        backup: true
        backup_options:
          filename: "{{ inventory_hostname }}-backup.cfg"
          dir_path: "{{ playbook_dir }}/backup-configs"

```
