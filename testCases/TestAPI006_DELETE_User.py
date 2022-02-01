import requests

payload = {
    "name": "morpheus_Automation",
    "job": "leader_Automation"
}

resp = requests.delete("https://reqres.in/api/users/2", data=payload)
print(resp.json())
print(resp.status_code)
assert resp.status_code == 204, "Deletion Fail"
