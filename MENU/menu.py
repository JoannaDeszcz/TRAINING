
import math

def pole_kwadratu(a):
    return a * a

def pole_prostokata(a, b):
    return a * b

def pole_kola(r):
    return math.pi * r ** 2

def pole_trojkata(a, h):
    return 0.5 * a * h

def pole_trapezu(a, b, h):
    return (a + b) / 2 * h

while (True):   
    wybor = int(input("""

    MENU 

    Wybierz figurę, której pole chcesz obliczyć:
    1. Kwadrat
    2. Prostokąt
    3. Koło
    4. Trójkąt
    5. Trapez

    Figura: """))

    if (wybor == 1):
        a = float(input("Podaj bok kwadratu: "))
        if(a>0):
            print("Pole kwadratu wynosi:", pole_kwadratu(a))
        else:
            print("Nie możnawykonać działania. Długość boku musi być liczbą dodatnią. Spróbuj jeszcze raz ") 
    elif (wybor == 2):
        a = float(input("Podaj pierwszy bok prostokąta: "))
        b = float(input("Podaj drugi bok prostokąta: "))
        if(a,b>0):
            print("Pole prostokąta wynosi:", pole_prostokata(a, b))
        else:
            print("Nie możnawykonać działania. Długość boku musi być liczbą dodatnią. Spróbuj jeszcze raz ") 
    elif (wybor == 3):
        r = float(input("Podaj promień koła: "))
        if(r>0):
            print("Pole koła wynosi:", pole_kola(r))
        else:
            print("Nie możnawykonać działania. Długość promienia musi być liczbą dodatnią. Spróbuj jeszcze raz ")
    elif (wybor == 4):
        a = float(input("Podaj bok trójkąta: "))
        h = float(input("Podaj wysokość trójkąta: "))
        if(a,h>0):
            print("Pole trójkąta wynosi:", pole_trojkata(a, h))
        else:
            print("Nie możnawykonać działania. Długość boku i wysokoś muszą być liczbami dodatnimi. Spróbuj jeszcze raz ")
    elif (wybor == 5):
        a = float(input("Podaj pierwszy bok prostokąta: "))
        b = float(input("Podaj drugi bok prostokąta: "))
        h = float(input("Podaj wysokość trapezu: "))    
        if(a,b,h>0):
            print("Pole trapezu wynosi:", pole_trapezu(a, b, h))
        else:
            print("Nie możnawykonać działania. Długości boku i wysokoś muszą być liczbami dodatnimi. Spróbuj jeszcze raz ")