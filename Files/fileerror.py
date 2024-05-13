import os,sys

try: 
    fin=open("inexistent_filess",'r')
except:
    print("Error Opening the file:", sys.exc_info())

if os.access("inexistent_filewww",os.R_OK):
    fin=open("inexistent_filewww",'t')   
else:
    print("Error: file reading is not possible")