dict1={
    'Student Name':'Vishal Verma',
    'Student ID' : '1234566',
    'Country' : 'India',
    'State' : 'NSW',
    'City' : 'Sydney',
    'Area' : 'Sefton',
    'Zip' : '2162'

}

print(dict1)
for i in dict1:
    print(i)
for key,values in dict1.items():
    print(f'{key}--->{values}')

print(f'{dict1.get('State')}')

#print(f'{dict1.get("State")}')

print(f'{dict1.get('Country')}')

print(f' State: {dict1.get('State')}')


dict1['Color'] = 'Lol'
dict1['Color'] = 'Brown'
print(dict1)
dict1.pop('Color')
print(dict1)
print(len(dict1))
print(dict1['Area'])
print(type(dict1))
del dict1

try:
    print(dict1)
except NameError:
    print("Data is gone")


dict2=dict(name='Vishal', age=10, sex='male')
print(dict2)

print(dict2.keys())

print(dict2.values())

dict2['location']='Sefton'
print(dict2.values())
dict2['location']='Auburn'
print(dict2.values())

print(dict2.items())

if 'name' in dict2:
    print(f' Yes it exit and it is {dict2.get('name')}')
else:
    print(f'no')