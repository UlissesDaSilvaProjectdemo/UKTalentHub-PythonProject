import requests

payload = {
    "name": "morpheus",
    "job": "leader"
}

print((type(payload)))
resp = requests.post("https://reqres.in/api/users", data=payload)
print(resp)
print(resp.json())

assert resp.json()["job"] == "leader", "valid job"
assert resp.json()["job"] == "no leader", "no valid job"
