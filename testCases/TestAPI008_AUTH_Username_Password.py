import requests

resp = requests.get("https://the-internet.herokuapp.com/basic_auth", auth=("admin", "admin"))
print(resp.status_code)
assert resp.status_code == 200, "Login success"
print(resp.text)
