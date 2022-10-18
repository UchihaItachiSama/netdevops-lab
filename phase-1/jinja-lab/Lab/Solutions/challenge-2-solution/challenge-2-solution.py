#!/usr/bin/python3

from pprint import pprint as pp
from jsonrpclib import Server
from jinja2 import Template, Environment, FileSystemLoader
import ssl
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context

DEVICE_IPS = [
    'leaf1',
    'leaf2',
    'leaf3', 
    'leaf4', 
    'spine1', 
    'spine2', 
    'host1', 
    'host2'
]

# Update the credentials based on your Lab Setup
USERNAME = 'arista'
PASSWORD = 'arista'

TEMPLATE_FILE = "device-template.j2"

if __name__ == '__main__':
    switch_output = {}
    KEYS = ['lldpNeighbors', 'systemMacAddress', 'hostname']
    for device in DEVICE_IPS:
        switch_output[device] = {}
        switch = Server( "https://{}:{}@{}/command-api".format(
            USERNAME,
            PASSWORD,
            device
        ) )
        result = switch.runCmds('latest', ['show hostname', 'show version', 'show lldp neighbors'])

        for cmd_output in result:
            for key, value in cmd_output.items():
                if key in KEYS:
                    switch_output[device].update({key: value})

    j2_loader = FileSystemLoader(searchpath='./')
    j2_env = Environment(loader=j2_loader, trim_blocks=True)
    j2_template = j2_env.get_template(TEMPLATE_FILE)

    print(j2_template.render(devices=switch_output))