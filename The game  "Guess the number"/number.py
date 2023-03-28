searchedNumber=40
guessedNumber=0

while guessedNumber!=searchedNumber:
    guessedNumber=int(input("Guess number:"))

    if (guessedNumber==searchedNumber):
        print("Bravo! You guessed the number")
        break
    elif (guessedNumber>=0 and guessedNumber<=10):
        print("Unfortunately, the number is even higher")
    elif (guessedNumber>10 and guessedNumber<=20):
        print("Unfortunately, the number is even higher")
    elif(guessedNumber>20 and guessedNumber<=30):
        print("You are getting closer, the number is a little bigger")
    elif(guessedNumber>30 and guessedNumber<=35):
        print("You're almost...The number is even bigger")
    elif(guessedNumber>35 and guessedNumber<40):
        print(" Round up and you will be the winner")
    else:
        print("Try again...The numer is too big.")