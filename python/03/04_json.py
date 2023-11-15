import json

numbers=[2,3,5,7,11,13]

filename="03/numbers.json"
with open(filename,'w') as file_object:
  json.dump(numbers,file_object)

with open(filename) as file_object:
  numbers2=json.load(file_object)

print(numbers2)   

fileJson="03/person.json"
with open(fileJson) as file_object:
  data=json.load(file_object)
  person_info=data.get("person",{})

print(data)
print(person_info)
