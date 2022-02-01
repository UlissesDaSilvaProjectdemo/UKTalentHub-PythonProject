import requests

payload = {
    "name": "morpheus_Automation",
    "job": "leader_Automation"
}

resp = requests.patch("https://reqres.in/api/users/2", data=payload)
print(resp)
print(resp.json())

#Assertion
assert resp.status_code == 200, "User update Failed"
