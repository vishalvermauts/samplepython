import re

fin=open('web.html')
fout=open('new.html',"w")

for line in fin:
    line=re.sub('<p>','<b>',line)
    line=re.sub('</p>','',line)
    fout.write(line)

fout.close()
