SecretNumber = 10
i = 0
maxGuess = 3

while i < maxGuess:
    Guess = int(input("Enter a number of your guess(1-10): "))
    if Guess != SecretNumber:
        i = i + 1
        print("Wrong! Try again please.")
    else:
        print("Correct! congrats you made the correct guess")
        i = i + 3
