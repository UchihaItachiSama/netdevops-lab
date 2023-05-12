# Demo

## Demo-1

Using the `arista.eos.eos_command` module we will get the output of some commands from the DC switches

### Playbook-1

```yaml
% cat eos_command_play.yml

---
- name: Demo play LEAF switches
  hosts: leafs
  gather_facts: false
  tasks:
    - name: Run command
      arista.eos.eos_command:
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
      arista.eos.eos_command:
        commands:
          - show clock
          - show hostname
      register: result
    - name: Print command output
      debug:
        msg: "{{ result.stdout_lines }}"

% ansible-playbook -i inventory.yml eos_command_play.yml
```

## Demo-2

### Playbook-2

Using the `ansible.builtin.uri` module we will send a HTTPS GET request to a URL and print the result.

```yaml
% cat uri_play.yml

---
- name: Demo ansible.builtin.uri module
  hosts: localhost
  gather_facts: false
  vars:
    city: California
  tasks:
    - name: Check the weather for city {{ city }}
      ansible.builtin.uri:
        url: "https://goweather.herokuapp.com/weather/{{ city }}"
        method: GET
        validate_certs: no
        body: '{}'
      register: result
      until: result.status == 200
      retries: 10
      delay: 10
    - name: Print weather result for city {{ city }}
      debug:
        msg:
          - "The weather forecast in {{ city }} right now is '{{ result.json.description | lower }}' with"
          - "temperature of {{ result.json.temperature }} and wind {{ result.json.wind }}"

% ansible-playbook uri_play.yml
```

## Demo-3

Using the `ansible.builtin.file` module we will create a directory and clone a repository from github using `ansible.builtin.git` into the created directory.

### Playbook-3

```yaml
% cat file_play.yml

---
- name: Demo ansible.builtin.file and ansible.builtin.git modules
  hosts: localhost
  gather_facts: false
  tasks:
    - name: Create a directory if it does not exists
      ansible.builtin.file:
        path: ./training
        state: directory
        mode: '0755'
    - name: Clone 'cvprac' into above directory
      ansible.builtin.git:
        repo: https://github.com/aristanetworks/cvprac
        dest: ./training/cvprac
        clone: yes

% ansible-playbook file_play.yml
```

## Demo-4

Using the `ansible.builtin.template` module we will render switch CLI configuration using YAML input and Jinja2 Template.

### Jinja2 Template

```jinja
{#- Ethernet Interface #}
{% if ethernet_interfaces is defined %}
{%     for ethernet_interface in ethernet_interfaces | sort %}
!
interface {{ ethernet_interface }}
{%         if ethernet_interfaces[ethernet_interface].description is defined %}
   description {{ ethernet_interfaces[ethernet_interface].description }}
{%         endif %}
{%         if ethernet_interfaces[ethernet_interface].type is defined and ( ethernet_interfaces[ethernet_interface].type | lower ) == 'routed' %}
   no switchport
{%             if ethernet_interfaces[ethernet_interface].ip_address is defined %}
   ip address {{ ethernet_interfaces[ethernet_interface].ip_address }}
{%             endif %}
{%         endif %}
{%     endfor %}
{% endif %}
```

### YAML Input

```yaml
---
ethernet_interfaces:
  Ethernet1:
    description: Uplink to DC1-Spine1
    type: routed
    ip_address: 10.10.0.1/30
  Ethernet2:
    description: Uplink to DC1-Spine2
    type: routed
    ip_address: 10.10.0.5/30
  Ethernet3:
    description: Uplink to DC1-Spine3
    type: routed
    ip_address: 10.10.0.9/30
```

### Playbook-4

```yaml
- name: Demo ansible.builtin.template module
  hosts: localhost
  gather_facts: false
  tasks:
    - name: Load variables from file
      ansible.builtin.include_vars:
        file: ./vars.yml
    - name: Generate configuration
      ansible.builtin.template:
        src: ./template.j2
        dest: ./DC1-Leaf1.cfg

```
