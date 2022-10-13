# CVP REST APIs Challenge Solutions

## Challenge-1

- Delete any existing session cookie files

```shell
rm <file-name>

example: rm cookiefile
```

- Authenticate and obtain a new session cookie from CVP and store it into file named `cvpcookiefile`

```shell
url -k -X POST -H 'Content-Type: application/json' \
 -d '{"userId":"arista","password":"arista"}' \
 https://cvp/cvpservice/login/authenticate.do \
 -c cvpcookiefile
```

## Challenge-2

- Get the list of all containers currently on CVP

```shell
curl -k -X GET -b cvpcookiefile \
"https://cvp/cvpservice/inventory/containers" \
-H "accept: application/json" | jq
```

## Challenge-3

- List of all devices that are in CVP inventory

```shell
curl -k -X GET -b cookiefile \
"https://cvp/cvpservice/inventory/devices" \
-H "accept: application/json" | jq
```

## Challenge-4

- Get all configlets on CVP

```shell
curl -k -X GET -b cvpcookiefile \
"https://cvp/cvpservice/provisioning/v3/getConfiglets.do?startIndex=0&endIndex=0&lightRead=true" \
-H "accept: application/json" | jq
```

## Challenge-5

- Get list of all devices under container named `Leaf`

```shell
curl -k -X GET -b cvpcookiefile \
"https://cvp/cvpservice/provisioning/getNetElementList.do?nodeId=container_12463e1d-8af6-43fa-986a-e4e249fd62df&startIndex=0&endIndex=0&ignoreAdd=true" \
-H "accept: application/json" | jq
```
