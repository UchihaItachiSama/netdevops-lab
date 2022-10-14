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

node = pyeapi.connect(host='192.168.0.12', username='arista', password='arista', return_node=True)

response = node.enable('show version')

pp(response)