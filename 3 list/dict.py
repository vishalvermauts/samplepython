my_dict= {
    "student":"Vishal",
    "StudentID" : 25042692,
    "Mark": 100,
    'Subject':'Unix'


}

print(my_dict)

value = my_dict["Mark"]
print(value)

my_dict["Mark"]-=10

print(my_dict)

my_dict["Course"] = "USP AND PYTHON"

print(my_dict)

del my_dict["Course"]


print(my_dict)


for item in my_dict:
    print(item)

for item in my_dict:
    print(my_dict[item])

for key,value in my_dict.items():
    print(f'{key} : {value}')

if 'student1' in my_dict:
    print("Yes Vishal is hrer")
else:
    print(f'no')