import sys
#1
#zadanie stworzyć funkcje wczytujaca plik i ma robic takie rzeczy: Wczytać plik do odczyt, przeczytać pierwsza linie pliku, przekonwertować ciag znaków do calkowitoliczbowego, wyrzucić 2 wyjątki, jakoe to nie pamiętam, jesli istnieje inny wyjątek to ma wypisać 'niespodzianka' i rzucić wyjątkiem, gdy nie ma wyjątki wypisać 'super'. Byly jeszcze jakies 2 podpunkty (odnośnie zakończenia chyba)
def funkcja():
    f=open("plik.txt", "r")
    pierwsza=f.readline()
    try:
        pierwsza=int(pierwsza)
    except ValueError:
        print("nie mozna przekonwertowac")
    except OSError:
        print("jakis blad")
    except:
        print("Inny:", sys.exc_info()[0])
    else:
        print("SUPER")

#2
#Klasa glowna owoc z metoda smacznosc, konstruktorem oraz atrybutami masa i nazwa.metoda smacznosc ma wypisac 0. Klasa arbuz dziedziczy po owoc. Ma konstruktor oraz zmienna prywatna liczbapestek o wartości 100. Nadpisuje metodę smacznosc i daje jej wartość 100. Klasa jabłko dziedziczy po owoc, zmienna liczbapestek ma wartość 10. Nadpisuje metodę smacznosc i daje jej wartość 10+liczbapestek. Cos ma to wszystko jeszcze na końcu robic.
