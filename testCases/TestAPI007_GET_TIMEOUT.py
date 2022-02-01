import requests

p = {"delay": 10}

resp = requests.get("https://reqres.in/api/users", params=p, timeout=7)
print(resp)
print(resp.json())
print(resp.headers.get("Content-TYpe"))
print(resp.status_code)
