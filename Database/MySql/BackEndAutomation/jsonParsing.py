import json

courses = '{"name": "RahulShetty","languages": [ "Java", "Python"]}'

#Loads method parse json string and it returns dictionary
dict_courses = json.loads(courses)
print(type(dict_courses))
print(dict_courses)
print(dict_courses['name'])
#get me the first language taught by trainer
# list_language = dict_courses['languages']
# print(type(list_language))
# print(list_language[0])
print(dict_courses['languages'][0])

#****** Parse content present in Json file
with open('C:\\Users\\Owner\\Documents\\course.json') as f:
    data = json.load(f)
    print(data)
    print(type(data))
    print(data['courses'][1]['title'])
    print(data['dashboard']['website'])
    print(type(data['dashboard']))
#price of course 'RPA'
    print(type(data['courses']))
    for course in data['courses']:
        #print(course)
        if course['title'] == "RPA":
            print(course['price'])
            assert course['price'] ==  45

with open('C:\\Users\\Owner\\Documents\\course1.json') as fi:
    data2 =  json.load(fi)
    assert data == data2

















