# Ansible Inventory Lab

In this lab your skills will be tested on what you have learned about Ansible Inventory.

## Challenge-1

Create two inventory files (one in `YAML` and other in `INI` format) for following devices:

| Device |
| ------ |
| spine1 |
| spine2 |
| leaf1 |
| leaf2 |
| leaf3 |
| leaf4 |
| host1 |
| host2 |
| cvp |
| cvx |

## Challenge-2

Further build upon the same inventory files to add the IP addresses for each of the clients.

| Device | MGMT_IP |
| ------ | ------- |
| spine1 | 192.168.0.10 |
| spine2 | 192.168.0.11 |
| leaf1 | 192.168.0.12 |
| leaf2 | 192.168.0.13 |
| leaf3 | 192.168.0.14 |
| leaf4 | 192.168.0.15 |
| host1 | 192.168.0.16 |
| host2 | 192.168.0.17 |
| cvp | 192.168.0.5 |
| cvx | 192.168.0.18 |

## Challenge-3

Update the same inventory files and group the devices as follows:

| Group | Members |
| ----- | ------- |
| spines | spine1, spine2 |
| rack01 | leaf1, leaf2 |
| rack02 | leaf3, leaf4 |
| clients | host1, host2 |
| cloudvision | cvp, cvx |
| leafs | rack01, rack02 |
| fabric | spines, leafs, clients, cloudvision |
| all | fabric |

## Challenge-4

Further build upon the inventory files to add the username and passwords for each device.

For all spine, leaf & clients the credentials are:

```yaml
username: arista
password: arista 
```

For `cvp` and `cvx` node the credentials are:

```yaml
username: root
password: toor
```
