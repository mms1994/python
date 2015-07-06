#6
def zmien(str):
    str2=""
    for i in range(len(str)):
        if str[i].isupper():
            str2+=str[i].lower()
        elif str[i].islower():
            str2+=str[i].upper()
        else:
            str2+=str[i]
    return str2

stri="oKeJ1OkEj2"
stri2=zmien(stri)
print(stri2)

#8
def dni(miesiac, rok):
    if (miesiac>0 and miesiac<13 and rok>0):
        if(miesiac==1 or miesiac==3 or miesiac==5 or miesiac==7 or miesiac==8 or miesiac==10 or miesiac ==12):
            return 31
        elif(miesiac==2):
            if(rok%4==0):
                if(rok%100==0):
                    if(rok%400==0):
                        return 29
                    else:
                        return 28
                else:
                    return 29
            else:
                return 28
        else:
            return 30
    else:
        return 0; #error
print(dni(2,1900))