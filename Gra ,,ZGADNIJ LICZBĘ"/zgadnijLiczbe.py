szukanaLiczba=40

zgadywanaLiczba=0

while zgadywanaLiczba!=szukanaLiczba:
    zgadywanaLiczba=int(input("Odgadnj liczbę:"))
    
    if (zgadywanaLiczba==szukanaLiczba):
        print("BRAWO! Odgadłeś liczbę")
    elif (zgadywanaLiczba>10 and zgadywanaLiczba<=20):
        print("Niestety, liczba jest jeszcze większa")
    elif(zgadywanaLiczba>20 and zgadywanaLiczba<=30):
        print("Jesteś coraz bliżej, liczba jest troche większa")
    elif(zgadywanaLiczba>30 and zgadywanaLiczba<=35):
        print("Juz prawie...Liczba jest jeszcze większa")
    elif(zgadywanaLiczba>35 and zgadywanaLiczba<40):
        print(" Zaokraglij w górę i zostaniesz zwyciężcą")
    else:
        print("Spróbuj jeszcze raz... LIczba jest zdecydowanie za mała")
