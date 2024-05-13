import struct

fout=open("test.bin",'wb')

number = 239.43

fout.write(struct.pack('d',number))
fout.close()
