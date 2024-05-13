import struct
import os

fout=open('test1.bin',"wb")

login='vishal'
fname='Vishal'
lname='Verma'
value=1020.567

fout.write(struct.pack("118s200s200sd",bytes(login,'utf-8'),bytes(fname,'utf-8'),bytes(lname,'utf-8'),value))

login='John2024'
fname='John'
lname='VermaVermaVermaVermaVermaVerma'
value=-73

fout.write(struct.pack("118s200s200sd",bytes(login,'utf-8'),bytes(fname,'utf-8'),bytes(lname,'utf-8'),value))

fout.close()

fin=open("test1.bin","rb")
fin.seek(0,0)
position = fin.tell()
print(position)
fin.seek(1056,0)
position = fin.tell()
print(position)
fin.seek(-528,1)
position = fin.tell()
print(position)

[blogin,bfname,blname,value]=struct.unpack("118s200s200sd",fin.read(528))
print(str(blogin,'utf-8'))

print(value)