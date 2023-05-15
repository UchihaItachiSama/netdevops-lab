# Demo

## Demo-1

Create a new role called `arista_baseline` in your Ansible project using the `ansible-galaxy` command

```shell
% ansible-galaxy init arista_baseline

% tree arista_baseline
arista_baseline
├── defaults
│   └── main.yml
├── files
├── handlers
│   └── main.yml
├── meta
│   └── main.yml
├── README.md
├── tasks
│   └── main.yml
├── templates
├── tests
│   ├── inventory
│   └── test.yml
└── vars
    └── main.yml
```

Now we will define role variables, by updating the `vars/main.yml` file which we will use to generate the baseline config.

```yaml
---
# vars file for arista_baseline
dns_domain: testing.com
clock:
  timezone: UTC
ntp_servers:
  - 0.pool.ntp.org
  - time.google.com
static_routes:
  - destination_prefix: 0.0.0.0/0
    gateway: 192.168.0.1
name_servers:
  - 8.8.8.8
  - 1.1.1.1
aaa_root:
  sha512_password: $6$SV63cqAiZoy5nRCo$rXWc/CJSVBN17VtaxaZsvYbY4N4.OihJgZGonBsouKJpHZXIAEbvJAgopkvLQTFiqVYRg4.BX0BJGhD1QX.En.
local_users:
  admin:
    privilege: 15
    role: network-admin
    no_password: true

<-- snipped -->

```

Next, we will define the tasks in `tasks/main.yml` that our `arista_baseline` role will perform. For this example, we will create a task that generates a baseline configuration for the Arista switch using the Jinja2 template engine.

```yaml
---
# tasks file for arista_baseline
- name: Create target folder
  file:
    path: "{{ playbook_dir }}/configs"
    state: directory
    mode: '0755'
  run_once: true
- name: Generate baseline configuration for {{ inventory_hostname }} Arista switch
  template:
    src: baseline.j2
    dest: "{{ playbook_dir }}/configs/{{ inventory_hostname }}_baseline.cfg"
  delegate_to: localhost
```

Next, we will create the `templates/baseline.j2` file to render the CLI config.

```jinja
!
! Management Access
interface Management1
   ip address {{ ansible_host }}/24
!
! Management Routes
{% for static_route in static_routes | sort %}
ip route {{ static_route.destination_prefix }} {{ static_route.gateway }}
{% endfor %}
!
hostname {{ inventory_hostname }}
!
! NTP Servers
{% for ntp_server in ntp_servers | sort %}
ntp server {{ ntp_server }}
{% endfor %}
!
clock timezone {{ clock.timezone }}
!
! Name Servers
{% for name_server in name_servers | sort %}
ip name-server {{ name_server}}
{% endfor %}
!
dns domain {{ dns_domain }}

<-- snipped -->
```

Now that we have defined our `arista_baseline` role, we can use it in a playbook. 

```yaml
---
- name: Demo Playbook using arista_baseline role
  hosts: leafs, spines
  gather_facts: false
  roles:
    - arista_baseline
```

```shell
% ansible-playbook -i inventory.yml demo-1-play.yml

% tree configs 
configs
├── leaf1_baseline.cfg
├── leaf2_baseline.cfg
├── leaf3_baseline.cfg
├── leaf4_baseline.cfg
├── spine1_baseline.cfg
└── spine2_baseline.cfg

% cat configs/spine1_baseline.cfg | head -20
!
! Management Access
interface Management1
   ip address 192.168.0.10/24
!
! Management Routes
ip route 0.0.0.0/0 192.168.0.1
!
hostname spine1
!
! NTP Servers
ntp server 0.pool.ntp.org
ntp server time.google.com
!
clock timezone UTC
!
! Name Servers
ip name-server 1.1.1.1
ip name-server 8.8.8.8
!
```
