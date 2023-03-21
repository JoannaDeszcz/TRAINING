

class Slownik:

    def __init__(self, lista_wyrazow):
        self.lista_wyrazow=lista_wyrazow

    def dodaj_wyraz(self):
        wyraz=input('\nPodaj słowo, które chcesz dodać: ')
        definicja =input('Podaj definicję: ')
        if wyraz not in self.lista_wyrazow:
            self.lista_wyrazow[wyraz]=definicja
            print(f'\nWyraz {wyraz} dodano do słownika!')
        else:
            print('\nPodane słowo już znajduję się w słowniku')
        
    def usun_wyraz(self):
        wyraz=input('Podaj słowo, które chcesz usunąć:')
        if wyraz in self.lista_wyrazow:
            del self.lista_wyrazow[wyraz]
            print(f'\nWyraz: {wyraz} został usunięty ze słownika!')
        else:
            print('\nPodany wyraz nie znajduje się w słowniku')

    def szukaj_wyrazu(self):
        wyraz=input('\nPodaj słowo, które chcesz wyszukać:')
        if wyraz in self.lista_wyrazow:
            print(f'{wyraz}:{self.lista_wyrazow[wyraz]}')
        else:
            print('\nPodany wyraz nie znajduje się w słowniku')

    def zobacz_slownik(self):
        print('\nOto twój słownik: \n')
        for wyraz, definicja in self.lista_wyrazow.items():
            print(f'\n {wyraz}:{definicja}') 
    
    

slownik=Slownik({'łóżko':'Na nim śpisz','boks':'sport'})

print('Hej, witaj w nowym słowniku')

while True:
    print('\nWybierz jaką czynność chcesz wykonać: \n\n1 - dodać wyraz \n2 - usunąc wyraz \n3 - wyszukać wyraz \n4 - zobaczyć słownik \n5 - zakończyć  ')
    wybor=int(input('\nWybrana czynność: '))

    if wybor==1:
        slownik.dodaj_wyraz()
    elif wybor==2:
        slownik.usun_wyraz()
    elif wybor==3:
        slownik.szukaj_wyrazu()
    elif wybor==4:
        slownik.zobacz_slownik()
    elif wybor==5:
        print('Słownik został zamknięty.')
        break







