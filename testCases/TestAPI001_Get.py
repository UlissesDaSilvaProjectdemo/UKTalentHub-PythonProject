import requests
# CRUDE
# Create = post
# Read = get
# Update = put/patch
# Delete = delete

p = {"page": 2}  # set the end point to parameter
resp = requests.get("https://reqres.in/api/users", params=p)
print(resp.url)  # print the response URL

# get server data
print(resp)
print(type(resp))
print(dir(resp))
code = resp.status_code
assert code == 200, "Code doesn't match"
print(resp.text)
print(resp.content)
print(resp.json())

print("SPACE   ------ //------  ")

# get user data
json_response = resp.json()
print(json_response["total"])

assert json_response["total"] == 12, "Total pages is matching"
print(json_response["total"])

assert json_response["total_pages"] == 2, "total pages counts is not matching"
print(json_response["total"])

print(json_response["data"][0]["email"])
assert (json_response["data"][0]["email"]).endswith("reqres.in"), "Email is valid"
# assert (json_response["data"][0]["email"]).endswith("reqres.in.com"),"Email format is not matching "

print(json_response["data"][2]["last_name"])
assert (json_response["data"][2]["last_name"]) is not None

print(json_response["support"]["text"])
