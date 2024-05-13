fout=open("vishal.txt","w")

number = 1234.567

fout.write(str(number))

list=['vishal','verma']

string='Hi How are You'
fout.write(str(string))

fout.write(str(list))

fout.close()

fin=open('web.html')

text = fin.readlines()

fin.close()

#fin.readlines()


print(text)