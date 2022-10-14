# Demo

## Demo-1

JSON example with various data types:

`String` and `Number`
```json
{
    "modelName": "cEOSLab",
    "memTotal": 59671872,
    "mfgName": "Arista",
    "systemMacAddress": "00:1c:73:b2:d5:01",
    "memFree": 26922580,
    "version": "4.28.1F-27567444.4281F (engineering build)",
    "hwMacAddress": "00:00:00:00:00:00",
    "architecture": "i686"
}
```

`Boolean` and `Object`

```json
{
    "clockSource": {
        "local": false,
        "ntpServer": "192.168.0.1"
    },
    "timezone": "UTC",
    "utcTime": 1665721768.831345,
    "localTime": {
        "dayOfWeek": 4,
        "dayOfYear": 287,
        "sec": 28,
        "min": 29,
        "hour": 4,
        "year": 2022,
        "dayOfMonth": 14,
        "daylightSavingsAdjust": 0,
        "month": 10
    }
}
```

`Arrays`

```json
{
    "dynamicEntries": 2,
    "ipV4Neighbors": [
        {
            "hwAddress": "02b8.9fa2.5835",
            "address": "192.168.0.1",
            "interface": "Management0",
            "age": 0
        },
        {
            "hwAddress": "001c.73a0.c601",
            "address": "192.168.0.5",
            "interface": "Management0",
            "age": 79
        }
    ],
    "notLearnedEntries": 0,
    "totalEntries": 2,
    "staticEntries": 0
}
```

Get JSON output of commands from EOS CLI

```json
leaf1#show ip int brief | json
{
    "interfaces": {
        "Management0": {
            "name": "Management0",
            "interfaceStatus": "connected",
            "interfaceAddress": {
                "ipAddr": {
                    "maskLen": 24,
                    "address": "192.168.0.12"
                }
            },
            "ipv4Routable240": false,
            "lineProtocolStatus": "up",
            "mtu": 1500
        }
    }
}
```
