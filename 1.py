import os
os.system("clear")

f = open("raqamlar.txt","rt")
ls = f.read().split()
f.close()
s = 0
for i in ls:
	s += int(i)
print(s)
