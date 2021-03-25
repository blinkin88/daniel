print("Jeśli chcesz policzę za ciebie kiedy będziesz miał setne urodziny!")
imię = input("Podaj swoje imię: ")
wiek = input("Podaj ile masz lat: ")
wiek = float(wiek)
wiek_test = int(wiek)
wiek_test = float(wiek_test)
if (wiek != wiek_test):
    print("Albo się pomyliłeś albo jesteś głupi - swój wiek podajemy pełnymi latami!")
    wiek = input("Proszę, podaj ile masz lat, SKUP SIĘ, powolutku: ")
    wiek = int(wiek)
else:
    wiek = int(wiek)
kiedy_urodziny = 2121 - wiek
kiedy_urodziny = str(kiedy_urodziny)
print("Super sprawa " + imię + " w " + kiedy_urodziny + " roku będziesz miał 100 lat")

print("Hej, a teraz mój system obliczeniowy sprawdzi czy podana przez ciebie liczba jest parzysta")
print("Od razu sprawdzę też czy dzieli się przez 4")
x = input("Podaj jakąś liczbę: ")
y = float(x)
r = y % 2
if (r == 1):
    print("Wpisałeś liczbę niepażystą, koniec gry")
else:
    print("Brawo, wpisałeś liczbę parzystą, + 5 punktów!")
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
    print("Brawo, to też się dzieli przez siebie, +3 punkty.")
else:
    print("Chujnia, te liczby są niepodzielne, - 4 punkty.")
