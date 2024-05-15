var='vishal'

name=' here'
list = [7, 11.2, 'some text', var]

print(list[::1])
print(list)
list[2] +=name
list[0]+=-119*3
print(list[-1])
for item in list:
    print(item)

for i in range(len(list)):
    print(list[i])


print(f'my name is:' , list[-1])
print(list[1:5])
print(list[:5:2])
print(list[3:])
print(list[:3])


list=[9,8,'hello',11,11119,-2,0]

list1=list+list
print(list1)

list1.reverse()

print((list1))

list2= ['apple','mango','beans','cherry','zappto']
list3=[-2,0,55,22,33,10,0,-34,-99]

print(sorted(list2))

list2.sort()

print(list2)

list.reverse()
print(list)

list3.sort()
print(list3)

if 900 in list3:
    print("Yes 22 is there")
else:
    print("No it not here")

list2.append('watermelon')
print(list2)
print(len(list2))
print(list2[len(list2)-1])
print(list2[-1])
print(list2[int(len(list2)/2)])

list2.insert(4,'banana')
print(list2)
list2.insert(-1,'banana')
print(list2)

list2.pop()
print(list2)
#list2.remove('banana')
#list2.remove('banana')
print(list2)
#list2.clear()
print(list2)

del list2
try:
    print(f'the List of fruits are', list2)
except NameError:
    print(f'List does not exist')