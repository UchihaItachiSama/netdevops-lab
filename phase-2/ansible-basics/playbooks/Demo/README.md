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
``

## Demo-3

### Playbook-3

```yaml
% cat file_play.yml

---
- name: Demo ansible.builtin.file and ansible.builtin.git modules
  hosts: localhost
  gather_facts: false
  tasks:
    - name: Creat a directory if it does not exists
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
