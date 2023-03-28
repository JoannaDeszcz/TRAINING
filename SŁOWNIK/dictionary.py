class Dictionary:

    def __init__(self, list_word):
        self.list_word=list_word

    def add_word(self):
        word=input('Specify the word you want to add: ')
        definition=input('Enter definition: ')
        if word not in self.list_word:
            self.list_word[word]=definition
            print(f'The word {word} has been added to the dictionary!')
        else:
            print('The word {word} is already in the dictionary')
        
    def delete_word(self):
        word=input('Enter the word you want to delete:')
        if word in self.list_word:
            del self.list_word[word]
            print(f'Word: {word} has been removed from the dictionary!')
        else:
            print('The specified word is not in the dictionary')

    def search_word(self):
        word=input('\nEnter the word you want to search for:')
        if word in self.list_word:
            print(f'{word}:{self.list_word[word]}')
        else:
            print('The specified word is not in the dictionary')

    def see_dictionary(self):
        print('\nThis is your dictionary: \n')
        for word, definition in self.list_word.items():
            print(f'{word}:{definition}') 
    
    

dictionary=Dictionary({'bed':'You sleep on it','box':'sport'})

print('Hey, welcome to the new dictionary')

while True:
    print('\nChoose what action you want to perform: \n\n1- add a word \n2 - delete a word \n3 - search for a word \n4 - view the dictionary \n5 - quit ')
    election=int(input('\nSelected action: '))

    if election==1:
        dictionary.add_word()
    elif election==2:
        dictionary.delete_word()
    elif election==3:
        dictionary.search_word()
    elif election==4:
        dictionary.see_dictionary()
    elif election==5:
        print('The dictionary has been closed.')
        break