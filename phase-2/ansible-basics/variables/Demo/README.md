# Demo

## Demo-1

In this demo we will see basic example of using variables in a playbook.

```shell
% tree demo-1/
demo-1
├── demo-1-play.yml
└── inventory.yml

% cd demo-1/

% ansible-playbook -i inventory.yml demo-1-play.yml

PLAY [Demo-1 Playbook] *********************************************************************************************************************

TASK [Print variables from playbook] *******************************************************************************************************
ok: [localhost] => {
    "msg": " Connecting to 'leaf1' using username 'arista' and password 'arista' "
}

PLAY RECAP *********************************************************************************************************************************
localhost                  : ok=1    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0

```

## Demo-2

In this demo we will see an example of loading variables from a file in a playbook.

```shell
% tree demo-2/
demo-2
├── custom_vars.json
├── custom_vars.yml
├── demo-2-play.yml
└── inventory.yml

% cd demo-2/

% ansible-playbook -i inventory.yml demo-2-play.yml

PLAY [Demo-2 Playbook] *********************************************************************************************************************

TASK [Print variables imported from files] *************************************************************************************************
ok: [localhost] => {
    "msg": [
        " Connecting to 'leaf1' using username 'arista' and password 'arista' ",
        " Connecting to 'leaf2' using username 'arista' and password 'arista' ",
        " Connecting to 'spine1' using username 'arista' and password 'arista' ",
        " Connecting to 'spine2' using username 'arista' and password 'arista' "
    ]
}

PLAY RECAP *********************************************************************************************************************************
localhost                  : ok=1    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0

```

## Demo-3

In this demo we will see an example of loading variables at runtime.

```shell
% tree demo-3/
demo-3/
├── demo-3-play.yml
└── inventory.yml

% cd demo-3/

% ansible-playbook -i inventory.yml demo-3-play.yml 
Enter the login username: cvpadmin
Enter the login password: 

PLAY [Demo-3 Playbook] *********************************************************************************************************************

TASK [debug] *******************************************************************************************************************************
ok: [localhost] => {
    "msg": "USER_INPUT ==> username is 'cvpadmin' & password 'arista' "
}

PLAY RECAP *********************************************************************************************************************************
localhost                  : ok=1    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0 

[ ANOTHER RUN USING --extra-vars OR -e ARGUMENT ]

% ansible-playbook -i inventory.yml demo-3-play.yml -e "username=cvpadmin"
Enter the login password: 

PLAY [Demo-3 Playbook] *********************************************************************************************************************

TASK [debug] *******************************************************************************************************************************
ok: [localhost] => {
    "msg": "USER_INPUT ==> username is 'cvpadmin' & password 'arista123' "
}

PLAY RECAP *********************************************************************************************************************************
localhost                  : ok=1    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

## Demo-4

In this demo we will see an example of registering a variable.

```shell
% tree demo-4/
demo-4
├── demo-4-play.yml
└── inventory.yml

% cd demo-4/

% ansible-playbook -i inventory.yml demo-4-play.yml 

TASK [Print command output] ****************************************************************************************************************
ok: [localhost] => {
    "result.stdout_lines": [
        "git version 2.30.2"
    ]
}
```

## Demo-5

In this demo we will see an example of `set_fact` module

```shell
% tree demo-5/
demo-5/
├── demo-5-play.yml
└── inventory.yml

% cd demo-5/

% ansible-playbook -i inventory.yml demo-5-play.yml

TASK [Print command result] ****************************************************************************************************************
ok: [localhost] => {
    "msg": "Device: 'spine1' || MGMT_IP: 192.168.0.10"
}
```

## Demo-6

In this demo we will see an example of loading variables from inventory file

```shell
% tree demo-6/
demo-6
├── demo-6-play.yml
└── inventory.yml

% cd demo-6/

% ansible-playbook -i inventory.yml demo-6-play.yml 

TASK [Testing variables from inventory] ****************************************************************************************************
ok: [leaf1] => {
    "msg": "Device: leaf1 || IP: 192.168.0.12 || Port: 22"
}
ok: [leaf2] => {
    "msg": "Device: leaf2 || IP: 192.168.0.13 || Port: 22"
}
ok: [leaf3] => {
    "msg": "Device: leaf3 || IP: 192.168.0.14 || Port: 22"
}
ok: [leaf4] => {
    "msg": "Device: leaf4 || IP: 192.168.0.15 || Port: 22"
}
```

## Demo-7

In this demo we will see an example of loading variables from `host_vars` and `group_vars` folders.

```shell
% tree demo-7/
demo-7
├── demo-7-play.yml
├── group_vars
│   └── fabric.yml
├── host_vars
│   ├── leaf1.yml
│   ├── leaf2.yml
│   ├── leaf3.yml
│   ├── leaf4.yml
│   ├── spine1.yml
│   └── spine2.yml
└── inventory.yml

% cd demo-7/

% ansible-playbook -i inventory.yml demo-7-play.yml

TASK [Testing variables from inventory] ****************************************************************************************************
ok: [leaf1] => {
    "msg": "Device: leaf1 || IP: 192.168.0.12 || Port: 443 || Username: cvpadmin || Password: arista"
}
ok: [leaf2] => {
    "msg": "Device: leaf2 || IP: 192.168.0.13 || Port: 443 || Username: cvpadmin || Password: arista"
}
ok: [leaf3] => {
    "msg": "Device: leaf3 || IP: 192.168.0.14 || Port: 443 || Username: cvpadmin || Password: arista"
}
ok: [leaf4] => {
    "msg": "Device: leaf4 || IP: 192.168.0.15 || Port: 443 || Username: admin || Password: arista123"
}
```
