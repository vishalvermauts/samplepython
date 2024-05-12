var='vishal'

name=' here'
my_list = [7, 11.2, 'some text', var]
print(my_list)
my_list[2] +=name
my_list[0]+=-119*3
print(my_list[-1])
for item in my_list:
    print(item)

for i in range(len(my_list)):
    print(my_list[i])


print(f'my name is:' , my_list[-1])
print(my_list[1:5])
print(my_list[:5:2])
print(my_list[3:])
print(my_list[:3])


list=[9,8,'hello',11,11119,-2,0]

list3=list+my_list
print(list3)

list3.reverse()

print((list3))

list9= ['apple','mango','beans','cherry','zappto']
list10=[-2,0,55,22,33,10,0,-34,-99]

print(sorted(list9))

list9.sort()

print(list9)

list.reverse()
print(list)

list10.sort()
print(list10)

if 900 in list10:
    print("Yes 22 is there")
else:
    print("No it not here")