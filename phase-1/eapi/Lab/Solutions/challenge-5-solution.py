#!/usr/bin/python3

from pprint import pprint as pp
from jsonrpclib import Server
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
    'host1', 
]

# Update the credentials based on your Lab Setup
USERNAME = 'arista'
PASSWORD = 'arista'

if __name__ == '__main__':
    for device in DEVICE_IPS:
        switch = Server( "https://{}:{}@{}/command-api".format(
            USERNAME,
            PASSWORD,
            device
        ) )
        result = switch.runCmds('latest', ['ping 172.16.112.202 repeat 10'], 'json')[0]
        print(result['messages'][0])