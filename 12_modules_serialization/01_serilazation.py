d="First File on serialization and deserialization"
with open('samp.txt', 'w') as f:
    f.write(d)


with open('samp.txt', 'r') as f:
    print(f.read())

#using dictionary
d1={
    "name":"Rahul",
     "age":20,
    "city":"Delhi"
    }
with open('sample.txt', 'w') as f:
    f.write(str(d1))

#Storing using json formate
import json

l1=[2, 23, 33, 4, 55]
with open('Sample1.json', 'w') as f:
    json.dump(l1 , f)

d1={
    "name":"Rahul",
     "age":20,
    "city":"Delhi"
    }
with open('sample2.json', 'w') as f:
    json.dump(d1 , f)

#Load function
with open('sample1.json', 'r') as f:
    l1=json.load(f)
    print(l1)