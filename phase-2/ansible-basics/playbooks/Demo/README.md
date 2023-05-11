# Demo

## Demo-1

Using the same `arista.eos.eos_command` module we will get the output of some commands from the DC switches

### Playbook

```yaml
---
- name: Demo play LEAF switches
  hosts: leafs
  gather_facts: false
  tasks:
    - name: Run command
      arista.eos.command:
        commands:
          - show version
          - show hostname
      register: result
    - name: Print command output
      debug:
        msg: "{{ result.stdout_lines }}"

- name: Demo play SPINE switches
  hosts: spines
  gather_facts: false
  tasks:
    - name: Run command
      arista.eos.command:
        commands:
          - show clock
          - show hostname
      register: result
    - name: Print command output
      debug:
        msg: "{{ result.stdout_lines }}"
```

## Demo-2

### Playbook

```yaml

```