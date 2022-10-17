#!/usr/bin/python3

from pprint import pprint as pp
from tkinter import Y
import yaml
from jinja2 import Template

template = """
!
hostname {{ hostname }}
!
ntp server {{ ntp.server }}
!
spanning-tree mode {{ spanning_tree.mode }}
!
service routing protocols model {{ service_routing_protocols_model }}
!
"""

JSON_INPUT = {
    "hostname": "leaf1",
    "ntp": {
        "server": "192.168.0.1"
    },
    "spanning_tree": {
        "mode": "mstp"
    },
    "service_routing_protocols_model": "multi-agent"
}

YAML_INPUT = '''
hostname: leaf1
ntp:
    server: 192.168.0.1
spanning_tree:
    mode: mstp
service_routing_protocols_model: multi-agent
'''

if __name__ == '__main__':
    j2_template = Template(template)
    print("\nRender using JSON input")
    print(j2_template.render(JSON_INPUT))

    print("\n\nRender using YAML input")
    yaml_dict = yaml.safe_load(YAML_INPUT)
    print(j2_template.render(yaml_dict))