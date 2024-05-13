
try:

    fin = open("data1.txt",'r')
    for i in fin:
        i=i.rstrip()
        print(i)
except FileNotFoundError:
    print("File Not Exist")