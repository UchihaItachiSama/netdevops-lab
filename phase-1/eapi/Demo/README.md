# Demo

## Demo-1

- As part of ATD Lab, eAPI would be enabled by default. If using a different setup, use the following configuration to enable it on all your lab devices

- From your `Programmability IDE` you can SSH into the switches using the hostname and username `arista`

```shell
➜ ssh arista@leaf1

Last login: Fri Oct 14 04:27:41 2022 from 192.168.0.1
leaf1#
leaf1#configure 
leaf1(config)#management api http-commands 
leaf1(config-mgmt-api-http-cmds)#no shutdown 
```

- Check if EAPI got enabled

```shell
#show management api http-commands 
Enabled:            Yes
HTTPS server:       running, set to use port 443
HTTP server:        shutdown, set to use port 80
Local HTTP server:  shutdown, no authentication, set to use port 8080
Unix Socket server: shutdown, no authentication
VRFs:               default
Hits:               0
Last hit:           never
Bytes in:           0
Bytes out:          0
Requests:           0
Commands:           0
Duration:           0.000 seconds
SSL Profile:        none
FIPS Mode:          No
QoS DSCP:           0
Log Level:          none
CSP Frame Ancestor: None
TLS Protocols:      1.0 1.1 1.2
URLs                                  
--------------------------------------
Management0 : https://192.168.0.12:443
```

## Demo-2

- Using `EapiClientLib` we will locally connect to EAPI and get output of few show commands
- Edit `demo-2.py` with relevant switch IP address and login credentials as per your ATD lab setup.
- Copy `demo-2.py` to any of the switches using `scp`

```shell
➜ scp demo-2.py arista@leaf1:/mnt/flash/   
```

- Login to switch using SSH and run the `demo-2.py` script

```shell
leaf1#bash python3 /mnt/flash/demo-2.py

{'id': 'FastCliSocketLib',
 'jsonrpc': '2.0',
 'result': [{'architecture': 'i686',
             'bootupTimestamp': 1665721454.499167,
             'cEosToolsVersion': '1.1',
             'configMacAddress': '00:00:00:00:00:00',
             'hardwareRevision': '',
             'hwMacAddress': '00:00:00:00:00:00',
             'imageFormatVersion': '1.0',
             'imageOptimization': 'None',
             'internalBuildId': 'aa54565c-ad3f-47c8-95a6-9b82f8bf7ad3',
             'internalVersion': '4.28.1F-27567444.4281F',
             'isIntlVersion': False,
             'kernelVersion': '5.4.132-1.el7.elrepo.x86_64',
             'memFree': 15344408,
             'memTotal': 59671872,
             'mfgName': 'Arista',
             'modelName': 'cEOSLab',
             'serialNumber': 'leaf1',
             'systemMacAddress': '00:1c:73:b2:d5:01',
             'uptime': 6848.221472978592,
             'version': '4.28.1F-27567444.4281F (engineering build)'}]}
leaf1#
```

## Demo-3

- Enable Unix domain socket.

```shell
➜  ssh arista@leaf1

Last login: Fri Oct 14 06:18:06 2022 from 192.168.0.1
leaf1#conf
leaf1(config)#management api http-commands 
leaf1(config-mgmt-api-http-cmds)#protocol unix-socket 

leaf1(config-mgmt-api-http-cmds)#show management api http-commands 
Enabled:            Yes
HTTPS server:       running, set to use port 443
HTTP server:        shutdown, set to use port 80
Local HTTP server:  shutdown, no authentication, set to use port 8080
Unix Socket server: running, no authentication
VRFs:               default
Hits:               0
Last hit:           never
Bytes in:           0
Bytes out:          0
Requests:           0
Commands:           0
Duration:           0.000 seconds
SSL Profile:        none
FIPS Mode:          No
QoS DSCP:           0
Log Level:          none
CSP Frame Ancestor: None
TLS Protocols:      1.0 1.1 1.2
URLs                                        
--------------------------------------------
Management0 : https://192.168.0.12:443      
Unix Socket : unix:/var/run/command-api.sock
```

- Edit `demo-3.py` with relevant switch IP address and login credentials as per your ATD lab setup.
- Copy `demo-3.py` to any of the switches using `scp`

```shell
➜ scp demo-3.py arista@leaf1:/mnt/flash/   
```

- Login to switch using SSH and run the `demo-3.py` script

```shell
leaf1#bash python /mnt/flash/demo-3.py

[{'architecture': 'i686',
  'bootupTimestamp': 1665721454.499167,
  'cEosToolsVersion': '1.1',
  'configMacAddress': '00:00:00:00:00:00',
  'hardwareRevision': '',
  'hwMacAddress': '00:00:00:00:00:00',
  'imageFormatVersion': '1.0',
  'imageOptimization': 'None',
  'internalBuildId': 'aa54565c-ad3f-47c8-95a6-9b82f8bf7ad3',
  'internalVersion': '4.28.1F-27567444.4281F',
  'isIntlVersion': False,
  'kernelVersion': '5.4.132-1.el7.elrepo.x86_64',
  'memFree': 15164844,
  'memTotal': 59671872,
  'mfgName': 'Arista',
  'modelName': 'cEOSLab',
  'serialNumber': 'leaf1',
  'systemMacAddress': '00:1c:73:b2:d5:01',
  'uptime': 7434.728924036026,
  'version': '4.28.1F-27567444.4281F (engineering build)'}]
leaf1#
```

## Demo-4

- In previous Demo's we were accessing EAPI locally from the switch.
- Now we will explore the command API via Web Browser i.e. off-the box access.
- From your lab page access `WebUI` and open `FireFox` web browser.
- Enter the following URL 

```shell
https://192.168.0.12:443
```

NOTE: To get the above URL, SSH into your switch and run the following command and look under `URLs` section

```shell
show management api http-commands 
```

- Click on Advanced --> Accept Risk and Continue to ignore warning about Self signed certificates
- When prompted for Username and Password, enter the Login credentials from the Lab Page.
- Enter the command `show version` and click on `Submit POST Request`

## Demo-5

- Similar to Demo-4 we will now try off-box EAPI access from a Python script.
- First example we will see is using `jsonrpclib` for this run the `demo-5.py` script

NOTE: Replace the login credentials as per your lab and IP address of the switch.

```shell
python3 demo-5.py

[{'architecture': 'i686',
  'bootupTimestamp': 1665721454.499167,
  'cEosToolsVersion': '1.1',
  'configMacAddress': '00:00:00:00:00:00',
  'hardwareRevision': '',
  'hwMacAddress': '00:00:00:00:00:00',
  'imageFormatVersion': '1.0',
  'imageOptimization': 'None',
  'internalBuildId': 'aa54565c-ad3f-47c8-95a6-9b82f8bf7ad3',
  'internalVersion': '4.28.1F-27567444.4281F',
  'isIntlVersion': False,
  'kernelVersion': '5.4.132-1.el7.elrepo.x86_64',
  'memFree': 14849872,
  'memTotal': 59671872,
  'mfgName': 'Arista',
  'modelName': 'cEOSLab',
  'serialNumber': 'leaf1',
  'systemMacAddress': '00:1c:73:b2:d5:01',
  'uptime': 8434.83861899376,
  'version': '4.28.1F-27567444.4281F (engineering build)'}]
```

## Demo-6

- Similar to Demo-5 we will now see another example using `pyeapi` library.
- For this demo run the `demo-6.py` script from this folder.

NOTE: Replace the login credentials as per your lab and IP address of the switch.

```shell
python3 demo-6.py

[{'command': 'show version',
  'encoding': 'json',
  'result': {'architecture': 'i686',
             'bootupTimestamp': 1665721454.499167,
             'cEosToolsVersion': '1.1',
             'configMacAddress': '00:00:00:00:00:00',
             'hardwareRevision': '',
             'hwMacAddress': '00:00:00:00:00:00',
             'imageFormatVersion': '1.0',
             'imageOptimization': 'None',
             'internalBuildId': 'aa54565c-ad3f-47c8-95a6-9b82f8bf7ad3',
             'internalVersion': '4.28.1F-27567444.4281F',
             'isIntlVersion': False,
             'kernelVersion': '5.4.132-1.el7.elrepo.x86_64',
             'memFree': 13351868,
             'memTotal': 59671872,
             'mfgName': 'Arista',
             'modelName': 'cEOSLab',
             'serialNumber': 'leaf1',
             'systemMacAddress': '00:1c:73:b2:d5:01',
             'uptime': 21665.564232110977,
             'version': '4.28.1F-27567444.4281F (engineering build)'}}]
```
