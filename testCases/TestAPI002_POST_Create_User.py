import requests

payload = {
    "first_name": "Byron",
    "last_name": "Fields",
    "id":"9"
}

print((type(payload)))
resp = requests.post("https://reqres.in/api/users", data=payload)
print(resp)
print(resp.json())

assert resp.json()["first_name"] == "Byron", "valid name"
assert resp.json()["last_name"] == "Fields", "no valid job"
