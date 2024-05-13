import os

fin=open("food.txt")

text=fin.read()

print(text)

print(repr(text))

print(len(text))

file_size = os.path.getsize("food.txt")

print(file_size)
try:
    fin2=open("drink.txt")
    text2=fin2.read()
    print(text2)
    print(repr(text2))
    print(len(text2))

    
    file_size2=os.path.getsize('drink.txt')
except FileNotFoundError:
    print("File Not Exist")

