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
