# Demo

## Demo-1

As part of this demo we will explore the CVP REST APIs from the CVP Swagger UI.

- Open the `CVP` from your AVD Web interface.
- Use the login credentials as per your AVD Lab.
- Once logged into CVP, head over to the Settings page by clicking on the Gear icon.
- From the settings page head over to the `REST API Explorer`
- Click on `Inventory` tab and from the dropdown click on the `GET /inventory/devices`
- Click on the `Try it out` button
- Click on `Execute` button

## Demo-2

As part of this Demo we will try out the CVP REST APIs from the `Terminal` of `Programmability IDE` to simulate an off-box REST API call.

- Click on `Programmability IDE`
- Open a terminal (Top-left lines icon > Terminal > New terminal)
- Use the authentication API to obtain a session cookie from the CVP

```shell
curl -k -X POST -H 'Content-Type: application/json' \
 -d '{"userId":"arista","password":"arista"}' \
 https://cvp/cvpservice/login/authenticate.do \
 -c ./cookiefile
```

- *Make sure to replace the username and password as per your AVD setup*
- You should now be able to see a cookie file created in your present directory
- Using this cookie file, now let's make an API call to the CVP to get the CVP version:

```shell
curl -k -X GET -b cookiefile \
 "https://cvp/cvpservice/cvpInfo/getCvpInfo.do" \
 -H "accept: application/json"
```

- Now let's get the device inventory similar to what we had done in Demo-1

```shell
curl -k -X GET -b cookiefile \
"https://cvp/cvpservice/inventory/devices" \
-H "accept: application/json" | python3 -m json.tool
```

- Note how the output is pretty printed.
- The same can be done using `jq`

```shell
curl -k -X GET -b cookiefile \
"https://cvp/cvpservice/inventory/devices" \
-H "accept: application/json" | jq
```

## Demo-3

- Get the CVP Version and device inventory using `cvprac` library in a python script.

```shell
python3 cvprac-demo.py
```

That's it for the Demo head over the `Lab` folder to test your padwan skills in CVP REST APIs.
