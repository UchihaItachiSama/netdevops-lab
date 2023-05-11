# Demo

## Demo-1

In this demo we will use the ad hoc command to run the `ping` module.

```shell
% ansible -m ping all -i inventory.yml
leaf1 | SUCCESS => {
    "changed": false,
    "ping": "pong"
}
host2 | SUCCESS => {
    "changed": false,
    "ping": "pong"
}
spine2 | SUCCESS => {
    "changed": false,
    "ping": "pong"
}
host1 | SUCCESS => {
    "changed": false,
    "ping": "pong"
}
spine1 | SUCCESS => {
    "changed": false,
    "ping": "pong"
}
leaf2 | SUCCESS => {
    "changed": false,
    "ping": "pong"
}
leaf3 | SUCCESS => {
    "changed": false,
    "ping": "pong"
}
leaf4 | SUCCESS => {
    "changed": false,
    "ping": "pong"
}
```

## Demo-2

In this demo we will run the arista eos_command module as ad hoc command for spine switches

```shell
% ansible -i inventory.yml spines -m arista.eos.eos_command -a "commands='show version'"
spine1 | SUCCESS => {
    "changed": false,
    "stdout": [
        "Arista cEOSLab\nHardware version: \nSerial number: spine1\nHardware MAC address: 001c.73b0.d501\nSystem MAC address: 001c.73b0.d501\n\nSoftware image version: 4.28.1F-27567444.4281F (engineering build)\nArchitecture: i686\nInternal build version: 4.28.1F-27567444.4281F\nInternal build ID: aa54565c-ad3f-47c8-95a6-9b82f8bf7ad3\nImage format version: 1.0\nImage optimization: None\n\ncEOS tools version: 1.1\nKernel version: 5.4.132-1.el7.elrepo.x86_64\n\nUptime: 1 hour and 6 minutes\nTotal memory: 59671872 kB\nFree memory: 16174172 kB"
    ],
    "stdout_lines": [
        [
            "Arista cEOSLab",
            "Hardware version: ",
            "Serial number: spine1",
            "Hardware MAC address: 001c.73b0.d501",
            "System MAC address: 001c.73b0.d501",
            "",
            "Software image version: 4.28.1F-27567444.4281F (engineering build)",
            "Architecture: i686",
            "Internal build version: 4.28.1F-27567444.4281F",
            "Internal build ID: aa54565c-ad3f-47c8-95a6-9b82f8bf7ad3",
            "Image format version: 1.0",
            "Image optimization: None",
            "",
            "cEOS tools version: 1.1",
            "Kernel version: 5.4.132-1.el7.elrepo.x86_64",
            "",
            "Uptime: 1 hour and 6 minutes",
            "Total memory: 59671872 kB",
            "Free memory: 16174172 kB"
        ]
    ]
}
spine2 | SUCCESS => {
    "changed": false,
    "stdout": [
        "Arista cEOSLab\nHardware version: \nSerial number: spine2\nHardware MAC address: 001c.73b1.d501\nSystem MAC address: 001c.73b1.d501\n\nSoftware image version: 4.28.1F-27567444.4281F (engineering build)\nArchitecture: i686\nInternal build version: 4.28.1F-27567444.4281F\nInternal build ID: aa54565c-ad3f-47c8-95a6-9b82f8bf7ad3\nImage format version: 1.0\nImage optimization: None\n\ncEOS tools version: 1.1\nKernel version: 5.4.132-1.el7.elrepo.x86_64\n\nUptime: 1 hour and 6 minutes\nTotal memory: 59671872 kB\nFree memory: 16174172 kB"
    ],
    "stdout_lines": [
        [
            "Arista cEOSLab",
            "Hardware version: ",
            "Serial number: spine2",
            "Hardware MAC address: 001c.73b1.d501",
            "System MAC address: 001c.73b1.d501",
            "",
            "Software image version: 4.28.1F-27567444.4281F (engineering build)",
            "Architecture: i686",
            "Internal build version: 4.28.1F-27567444.4281F",
            "Internal build ID: aa54565c-ad3f-47c8-95a6-9b82f8bf7ad3",
            "Image format version: 1.0",
            "Image optimization: None",
            "",
            "cEOS tools version: 1.1",
            "Kernel version: 5.4.132-1.el7.elrepo.x86_64",
            "",
            "Uptime: 1 hour and 6 minutes",
            "Total memory: 59671872 kB",
            "Free memory: 16174172 kB"
        ]
    ]
}
```
