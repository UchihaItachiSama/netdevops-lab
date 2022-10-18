# Jinja Lab

In this folder your skills will be tested on what you have learned about JINJA.

From the `Programmability IDE` perform the following operations.

## Challenge-1

- Using the following YAML as input

```yaml
radius_servers:
  - host: 192.168.0.1
    key: 0207165218120E
aaa_server_groups:
  - name: atds
    type: radius
    servers:
      - server: 192.168.0.1
aaa_authentication:
  login:
    default: group atds local
aaa_authorization:
  exec:
    default: group atds local
  commands:
    all_default: local
```

- Build a JINJA2 template to generate the following CLI output:

```shell
!
radius-server host 192.168.0.1 key 7 0207165218120E
!
aaa group server radius atds
   server 192.168.0.1
!
aaa authentication login default group atds local
aaa authorization exec default group atds local
aaa authorization commands all default local
!
```
