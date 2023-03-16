print("Hej, witaj w nowym słowniku","\n")
słownik={'łóżko':'Na nim śpisz','boks':'sport'}
i=0

while (i<1000):
    print("Wbierz, jaką czynność chcesz wykonać:  ")
    wybór=input(" 1 - dodać definicję 2 - usunąc definicję 3 - wyszukać definicji 4 - zobaczyć słownik :     ")
    if(wybór=="1"):
        definicja=słownik.update({input("Podaj słowo: "):input("Podaj definicje: ")})
        print("Definicję dodano do słownika!")
        print("DALEJ")
    elif(wybór=="2"):
        print("Podaj definicję, którą chcesz usunąć")
        del(słownik[input()])
        print("  ")
        print("Podaną definicję usunięto ze słownika")
        print("DALEJ")     
    elif(wybór=="3"):
        print("Podaj definicję, którą chcesz odnależć")
        print("  ")
        for key in słownik:
            print(input(),":",słownik[key])
        print("\n","Super! Twoja definicja została odnaleziona.")
        print("DALEJ")
    elif(wybór=="4"):
        print("Oto Twój słownik")
        for key in słownik:
            print(key," : ",słownik[key])
        print("   ")
        print("DALEJ")
    else:
        print("Nie wybrałeś żadnej z możliwych odpowiedzi. Zamkyam słownik")
        break
