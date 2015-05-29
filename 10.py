#1
f = open("scr.txt", "r")
a=0
b=0
slownik={}
for line in f:
    temp=line.split(' ')
    if str(temp[0])=='set':
        slownik[temp[1]]=temp[2]
    print(a)
print(b)
print(slownik)
#2

#3
