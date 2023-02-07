import json
import requests

#myData = open("C:\\Users\\anshujit.mishra\\PycharmProjects\\UKTalentHub-PythonProject\\data.json", "r").read()
myData = open("C:\\Users\\Ulisses.Dasilva\\UKTalentHub-PythonProject\\data.json", "r").read()

resp = requests.post("https://reqres.in/api/users",
                     data=json.loads(myData))  # json.loads() -Deserialized and converts into object
print(resp)
print(resp.json())
assert resp.json()["first_name"] == "Michael", "valid name"

print(resp.headers.get("Content-Type"))
