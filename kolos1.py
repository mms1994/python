#1
def fLista():
    lista=[['ala', 5], [5,1], [3,1], ['kot', 'pies']]
    return lista
argumenty=fLista()
print(argumenty)
def usun(lista):
    for i in range(len(lista)):
        if int(lista[i][0]) % 3 != 0:
            lista.remove(i)
    return lista
#argumenty=usun(argumenty)
print(argumenty)
def wstaw(lista):
    for i in range(1,2*len(lista)-1,2):
        lista.insert(i, 'kot')
    return lista
argumenty=wstaw(argumenty)
print(argumenty)
def wypisz(lista):
    for i in range(len(lista)):
            print(lista[i])
wypisz(argumenty)
#2
def fib(k):
    if k <= 0:
        return 0
    elif k == 1:
        return 1
    else :
        return fib(k-1)+fib(k-2)

def slownikL(n):
    slownik={k:fib(k) for k in range(n)}
    return slownik

slow=slownikL(15)
print (slow)