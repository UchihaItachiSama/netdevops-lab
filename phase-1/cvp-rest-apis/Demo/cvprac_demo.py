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
    pp(client.api.get_cvp_info())
    pp(client.api.get_inventory())
