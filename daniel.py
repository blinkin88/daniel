print("Jeśli chcesz policzę za ciebie kiedy będziesz miał/a setne urodziny!")
import datetime
x = datetime.datetime.now()
imię = input("Podaj swoje imię: ")
wiek = input("Podaj ile masz lat: ")
wiek = int(wiek)
uro = input("Czy miałeś/aś już w tym roku urodziny? (tak/nie): ")
urodzinytak = x.year - wiek + 100
urodzinytak = str(urodzinytak)
urodzinynie = x.year - wiek + 99
urodzinynie = str(urodzinynie)
def funk1():
    if uro == ("tak"):
        print("Super sprawa. " + imię + " w " + urodzinytak + " roku będziesz miał/a 100 lat")
    else:
        print("Super sprawa. " + imię + " w " + urodzinynie + " roku będziesz miał/a 100 lat")
funk1()
print("Hej, a teraz mój system obliczeniowy sprawdzi czy podana przez ciebie liczba jest parzysta")
print("Od razu sprawdzę też czy dzieli się przez 4")
x = input("Podaj jakąś liczbę: ")
y = float(x)
r = y % 2
if (r == 1):
    print("Wpisałeś/aś liczbę niepażystą, koniec gry")
else:
    print("Brawo, wpisałeś/aś liczbę parzystą, + 5 punktów!")
    if (y % 4 == 0):
        print("Super, w dodatku da się ją podzielić przez 4, + 2 punkty.")
    else:
        print("Ale nie da się jej podzielić przez 4, - 2 punkty :(")
print("W ostatnim kroku sprawdzę czy podane przez ciebie liczby są podzielne")
q = input("Podaj jakąś kolejną liczbę: ")
w = input("I kolejną: ")
q = float(q)
w = float(w)
if (q % w == 0):
    print("Brawo, to się dzieli przez siebie, +3 punkty.")
else:
    print("Lipa, te liczby są niepodzielne, - 4 punkty.")
input()