import time
# 1
print (2 ** 7)
#2
dzien = input("podaj dzien")
print(dzien)
if dzien == "poniedziałek":
    print ("oto i poniedziałek")
elif dzien == "wtorek":
    print("oto i wtorek")
elif dzien == "środa":
    print("oto i środa")
elif dzien == "czwartek":
    print("oto i czwartek")
elif dzien == "piątek":
    print("oto i piątek")
elif dzien == "sobota":
    print("oto i sobota")
elif dzien == "niedziela":
    print("oto i niedziela")
else:
    for i in range(100):
        print("MO")
#3
def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=" ")
        a, b = b, a+b
fib(50)
#4
print(time.clock())
napisy=["napisy końcowe",
             "Kostiumy: natura",
             "Kamerowanie: brak",
             "Scenariusz: autor",
             "Podziekowania: Python",
             "Scenografia: autor"]
for i in range(len(napisy)):
    print(napisy[i].center(80, '#'))
    time.sleep(1)
print(time.clock())
#5
for i in range(len(napisy)):
    print(napisy[i].center(80, '#'))
    start=time.clock()
    koniec=time.clock()
    while ((koniec-start)<1):
        koniec=time.clock()
print(time.clock())