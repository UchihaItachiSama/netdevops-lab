# Ansible Inventory Lab Solutions

## Challenge-1

### INI

```ini
[all:hosts]
spine1
spine2
leaf1
leaf2
leaf3
leaf4
host1
host2
cvp
cvx
```

### YAML

```yaml
all:
  hosts:
    spine1:
    spine2:
    leaf1:
    leaf2:
    leaf3:
    leaf4:
    host1:
    host2:
    cvp:
    cvx:
```

## Challenge-2

### INI

```ini
[all:hosts]
spine1 ansible_host=192.168.0.10
spine2 ansible_host=192.168.0.11
leaf1 ansible_host=192.168.0.12
leaf2 ansible_host=192.168.0.13
leaf3 ansible_host=192.168.0.14
leaf4 ansible_host=192.168.0.15
host1 ansible_host=192.168.0.16
host2 ansible_host=192.168.0.17
cvp ansible_host=192.168.0.5
cvx ansible_host=192.168.0.18
```

### YAML

```yaml
all:
  hosts:
    spine1:
      ansible_host: 192.168.0.10
    spine2:
      ansible_host: 192.168.0.11
    leaf1:
      ansible_host: 192.168.0.12
    leaf2:
      ansible_host: 192.168.0.13
    leaf3:
      ansible_host: 192.168.0.14
    leaf4:
      ansible_host: 192.168.0.15
    host1:
      ansible_host: 192.168.0.16
    host2:
      ansible_host: 192.168.0.17
    cvp:
      ansible_host: 192.168.0.5
    cvx:
      ansible_host: 192.168.0.18
```

## Challenge-3

### INI

```ini
[all:children]
fabric

[fabric:children]
spines
leafs
clients
cloudvision

[spines:hosts]
spine1 ansible_host=192.168.0.10
spine2 ansible_host=192.168.0.11

[leafs:children]
rack01
rack02

[rack01:hosts]
leaf1 ansible_host=192.168.0.12
leaf2 ansible_host=192.168.0.13

[rack02:hosts]
leaf3 ansible_host=192.168.0.14
leaf4 ansible_host=192.168.0.15

[clients:hosts]
host1 ansible_host=192.168.0.16
host2 ansible_host=192.168.0.17

[cloudvision:hosts]
cvp ansible_host=192.168.0.5
cvx ansible_host=192.168.0.18
```

### YAML

```yaml
all:
  children:
    fabric:
      children:
        clients:
          hosts:
            host1:
              ansible_host: 192.168.0.16
            host2:
              ansible_host: 192.168.0.17
        cloudvision:
          hosts:
            cvp:
              ansible_host: 192.168.0.5
            cvx:
              ansible_host: 192.168.0.18
        leafs:
          children:
            rack01:
              hosts:
                leaf1:
                  ansible_host: 192.168.0.12
                leaf2:
                  ansible_host: 192.168.0.13
            rack02:
              hosts:
                leaf3:
                  ansible_host: 192.168.0.14
                leaf4:
                  ansible_host: 192.168.0.15
        spines:
          hosts:
            spine1:
              ansible_host: 192.168.0.10
            spine2:
              ansible_host: 192.168.0.11
```

## Challenge-4

### INI

```ini
[all:children]
fabric

[fabric:children]
spines
leafs
clients
cloudvision

[fabric:vars]
ansible_username=arista
ansible_password=arista

[spines:hosts]
spine1 ansible_host=192.168.0.10
spine2 ansible_host=192.168.0.11

[leafs:children]
rack01
rack02

[rack01:hosts]
leaf1 ansible_host=192.168.0.12
leaf2 ansible_host=192.168.0.13

[rack02:hosts]
leaf3 ansible_host=192.168.0.14
leaf4 ansible_host=192.168.0.15

[clients:hosts]
host1 ansible_host=192.168.0.16
host2 ansible_host=192.168.0.17

[cloudvision:hosts]
cvp ansible_host=192.168.0.5
cvx ansible_host=192.168.0.18

[cloudvision:vars]
ansible_username=root
ansible_password=toor
```

### YAML

```yaml
all:
  children:
    fabric:
      children:
        clients:
          hosts:
            host1:
              ansible_host: 192.168.0.16
            host2:
              ansible_host: 192.168.0.17
        cloudvision:
          hosts:
            cvp:
              ansible_host: 192.168.0.5
            cvx:
              ansible_host: 192.168.0.18
          vars:
            ansible_username: root
            ansible_password: toor
        leafs:
          children:
            rack01:
              hosts:
                leaf1:
                  ansible_host: 192.168.0.12
                leaf2:
                  ansible_host: 192.168.0.13
            rack02:
              hosts:
                leaf3:
                  ansible_host: 192.168.0.14
                leaf4:
                  ansible_host: 192.168.0.15
        spines:
          hosts:
            spine1:
              ansible_host: 192.168.0.10
            spine2:
              ansible_host: 192.168.0.11
      vars:
        ansible_username: arista
        ansible_password: arista
```
