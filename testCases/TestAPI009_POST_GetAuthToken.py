import requests

payload = {
    "email": "eve.holt@reqres.in",
    "password": "cityslicka"
}

resp = requests.post("https://reqres.in/api/login", data=payload)
print(resp.status_code)
assert resp.status_code == 200, "POST request failed"
print(resp.json())






