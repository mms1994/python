from math import sqrt
import builtins
import lab96
import lab95
import lab94

#1
lista=[sqrt(x) for x in range(13)]
print(lista)
print('')
#2
lista2=['mid or afk'[0:10-x] for x in range(10)]
print(lista2)
print('')
#3
list=dir(builtins)
liste=[]
for x in range(len(list)):
    if (list[x][0] in ['a', 'j', 'o', 'i', 'u', 'y', 'e']):
        liste.append(list[x])
for x in range(len(liste)):
    print(liste[x]+": "+str(len(liste[x])))
print('')
#4
lab94.pisz('gumijagody')
print('')
#5
lab95.pisz('gumijagody')
print('')
#6
lab96.pisz('gumijagody')