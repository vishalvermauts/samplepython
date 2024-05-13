import os
read=os.listdir(".")
read1=os.walk(".")
print("All the content as a list", read)
for item in read:
    print(item)
