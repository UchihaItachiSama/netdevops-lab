#!/usr/bin/python3

from pprint import pprint as pp
import pyeapi
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
    '192.168.0.10',
    '192.168.0.11',
    '192.168.0.12', 
    '192.168.0.13', 
    '192.168.0.14', 
    '192.168.0.15', 
    '192.168.0.16', 
    '192.168.0.17'
]

def get_hostname(node):
    result = node.enable('show hostname')
    return {"Hostname": result[0]['result']['hostname']}

def get_version_detail(node):
    result = node.enable('show version detail')
    return {"Model Name": result[0]['result']['modelName'],
            "Software Version": result[0]['result']['version'],
            "TerminAttr Version": result[0]['result']['details']['packages']['TerminAttr-core']['version'],
            "MAC Address": result[0]['result']['systemMacAddress']}

def get_mgmt_ip(node):
    result = node.enable('show version detail')

if __name__ == '__main__':
    for device in DEVICE_IPS:
        device_info = {}
        node = pyeapi.connect(host=device, username='arista', password='arista', return_node=True)
        device_info.update(get_hostname(node))
        device_info.update(get_version_detail(node))
        print(device_info)