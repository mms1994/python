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

