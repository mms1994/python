#1
f = open("scr.txt", "r")
a=0
b=0
slownik={}
line=f.readline()
while(line!=""):
    line=line.replace("\n", "")
    temp=line.split(' ')
    if str(temp[0])=='set':
        slownik[temp[1]]=temp[2]
    elif str(temp[0])=='add':
        slownik[temp[1]]=slownik[temp[1]]+slownik[temp[2]]
    line=f.readline()
print(slownik)
#2

#3
