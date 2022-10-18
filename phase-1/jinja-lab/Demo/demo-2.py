#!/usr/bin/python3

import yaml
from jinja2 import Template, Environment
import json

template = """
{% for interface in ethernet_interfaces %}
!
interface {{ interface }}
  description {{ ethernet_interfaces[interface].description }}
  {{ ethernet_interfaces[interface].type }}
  ip address {{ ethernet_interfaces[interface].ip_address }}
{% endfor %}
!
"""

JSON_INPUT = """
{
  "ethernet_interfaces": {
    "Ethernet2": {
      "description": "LEAF1",
      "type": "no switchport",
      "ip_address": "10.101.201.201/24"
    },
    "Ethernet3": {
      "description": "LEAF2",
      "type": "no switchport",
      "ip_address": "10.102.201.201/24"
    },
    "Ethernet4": {
      "description": "LEAF3",
      "type": "no switchport",
      "ip_address": "10.103.201.201/24"
    },
    "Ethernet5": {
      "description": "LEAF4",
      "type": "no switchport",
      "ip_address": "10.104.201.201/24"
    }
  }
}
"""

YAML_INPUT = '''
ethernet_interfaces:
  Ethernet2:
    description: LEAF1
    type: 'no switchport'
    ip_address: 10.101.201.201/24
  Ethernet3:
    description: LEAF2
    type: 'no switchport'
    ip_address: 10.102.201.201/24
  Ethernet4:
    description: LEAF3
    type: 'no switchport'
    ip_address: 10.103.201.201/24
  Ethernet5:
    description: LEAF4
    type: 'no switchport'
    ip_address: 10.104.201.201/24
'''

if __name__ == '__main__':
  j2_template = Template(template, trim_blocks=True)

  print("\nRender using JSON input")
  print(j2_template.render(json.loads(JSON_INPUT)))

  print("\nRender using YAML input")
  print(j2_template.render(yaml.safe_load(YAML_INPUT)))