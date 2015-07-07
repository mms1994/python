#1
print("zad1")
print(7/5)
print(7//5)
print(7%5)
print("poza zakresem")
print("poza zakresem")
print("nie mozna tak zrobic podmiany")
print("chuj wie, dużo przepisywania")
litery=['a', 'b', 'c', 'd']
litery[1]=321
print(litery)
#2
print("")
print("zad2")
def potrojenie(x):
    print('potrajanie', x)
    return x*3
def odejmij(y,z):
    print('odejmowanie', y, z)
    return y-z
if  odejmij(20, potrojenie(10)) > 0 and odejmij(-25, potrojenie(5)) >0:
    print('jejku!')
else:
    print('ojej!', odejmij(potrojenie(3), 0))

#3
print("")
print("zad3")
def zrob_cos(a,b):
    a.insert(0, 'd')
    b=['d']+b

a = ['a', 'b', 'c']
a1 = a
a2 = a[:]

b=['a', 'b', 'c']
b1=b
b2=b[:]

zrob_cos(a,b)

print(a)
print(a1)
print(a2)
print(b)
print(b1)
print(b2)

#4
print("")
print("zad4")
def tajemniczy_kod(b1, b2, i, s):
    if False:
        print("warunek 0")
    elif b1:
        print("warunek 1")
    if (b1 or b2) and i==4:
        if i>10:
            print("warunek 2")
        elif not b1:
            print("warunek 3")
        elif b1 and s=='':
            print("warunek 4")
        elif s==str(i):
            print("warunek 5")
        else:
            print("warunek 6")
#testujcie sobie :)

#5
print("")
print("zad5")
print("a: c")
print("b: b")

#6
print("")
print("zad6")
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

#7
print("")
print("zad7")
def length_dict(word_list):
    dict={}
    for i in range(len(word_list)):
        dict[len(word_list[i])]=word_list[i]
    return dict

word="ok", "aba"

dicte=length_dict(word)
print(dicte)

#8
print("")
print("zad8")
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

#9
print("")
print("zad9")
class Okrag:
    promien=0
    def __init__(self, pr):
        self.promien=pr
    def pole(self):
        return self.promien*self.promien*3.141593
    def drukuj(self):
        print("Okrąg".ljust(10), end="|")
        print("promień".ljust(10), end="|")
        print("pole")
        print("".ljust(10), end="|")
        print(str(self.promien).ljust(10), end="|")
        print(str(self.pole()).ljust(10))
a=Okrag(3)
a.drukuj()