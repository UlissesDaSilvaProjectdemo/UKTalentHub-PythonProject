import requests

payload = {
    "name": "morpheus_Automation_PATCH",
    "job": "leader_Automation_PATCH"
}

resp = requests.patch("https://reqres.in/api/users/2", data=payload)
print(resp)
print(resp.json())

#Assertion
assert resp.status_code == 200, "User update Failed"
