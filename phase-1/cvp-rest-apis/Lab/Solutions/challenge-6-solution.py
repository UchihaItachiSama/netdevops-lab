#!/usr/bin/python3

from pprint import pprint as pp
from cvprac.cvp_client import CvpClient
import ssl
ssl.create_default_https_context = ssl._create_unverified_context
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()

if __name__ == '__main__':
    client = CvpClient()
    client.connect(nodes=['cvp'], username="arista", password="arista")
    inventory = client.api.get_inventory()
    for device in inventory:
        print("Hostname: {} | Model Name: {} | EOS Version: {} | IP Address: {} | MAC Address: {}\n".format(
            device['hostname'], 
            device['modelName'],
            device['version'],
            device['ipAddress'],
            device['systemMacAddress']
        ))