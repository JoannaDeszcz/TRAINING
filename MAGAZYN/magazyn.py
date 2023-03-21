
# Tworzenie magazynu: dodanie produktów, usunięcie itp
import sys
class Magazyn:

    def __init__(self,lista_produktow):
        self.lista_produktow=lista_produktow

    def wyswietl_dostepne_produkty(self):
        print('Dostępne produkty: \n')
        for produkt in self.lista_produktow:
            print(produkt)
    
    def dodaj_produkt(self):
        self.nazwa_produktu=input('Podaj nazwę produktu, który chcesz dodać:  ')
        if self.nazwa_produktu not in self.lista_produktow:
            self.lista_produktow.append(self.nazwa_produktu)
            print(f'\nProdukt {self.nazwa_produktu} został oddany do magazynu. \n')
        else:
            ('\nTen produkt znajduję się już w magazynie. \n')

    def usun_produkt(self):
        self.nazwa_produktu=input('Podaj nazwę produktu, który chcesz usunąć: ')
        if self.nazwa_produktu in self.lista_produktow:
            self.lista_produktow.remove(self.nazwa_produktu)
            print(f'\nProdukt {self.nazwa_produktu} został usunięty z magazynu. \n')
        else: 
            print('\nPodanego produktu nie ma w magzynie. \n')

magazyn=Magazyn(['mleko','woda','jajka'])

print('Witaj w magazynie!')

while True:

    print('\nWybierz jaką czynność chcesz wykonać: \n\n1 - zobaczyć stan magazynu \n2 - dodać produkt \n3 - usunąć produkt \n4 - zakończ \n')
    wybor_uzytkownika=int(input('Wybrana czynność: '))

    if wybor_uzytkownika == 1:
        magazyn.wyswietl_dostepne_produkty()
    elif wybor_uzytkownika == 2:
        magazyn.dodaj_produkt()
    elif wybor_uzytkownika == 3:
        magazyn.usun_produkt()
    elif wybor_uzytkownika == 4:
        print('Zakończono pracę w magazynie')
        sys.exit()
    

