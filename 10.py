#1
f = open("scr.txt", "r")
a=0
b=0
slownik={}
line=f.readline()
while(line!=EOFError):
    line=line.replace("\n", "")
    temp=line.split(' ')
    if str(temp[0])=='set':
        slownik[temp[1]]=temp[2]
    elif str(temp[0])=='add':
        slownik[temp[1]]=int(slownik[temp[1]])+int(slownik[temp[2]])
    elif str(temp[0])=='mul':
        slownik[temp[1]]=int(slownik[temp[1]])*int(slownik[temp[2]])
    elif str(temp[0])=='print':
        print(slownik[temp[1]])
    elif str(temp[0])=='noop':
        continue
    elif str(temp[0])=='read':
        #wczytywanie
        continue
    line=f.readline()
#2

#3
