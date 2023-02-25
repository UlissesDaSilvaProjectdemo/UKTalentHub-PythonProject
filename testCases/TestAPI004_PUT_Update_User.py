import requests

# PUT update or replace exist record
# Patch - update only one exist property
payload = {
    "name": "morpheus_UKTALENTHUB",
    "job": "leader_UKTALENTHUB"
}

resp = requests.put("https://reqres.in/api/users/2", data=payload)
print(resp)
print(resp.json())

#Assertion
assert resp.status_code == 200, "User update Failed"
