secret = 22
guess = 0

while guess != secret:   # =! znači is not equal
    guess = int(input("Guess the secret number (between 1 and 30: "))
    if guess == secret:
        print("Congratulations, it's number 22!")
    else:
        print("Sorry, your guess is not correct... The secret number is not " + str(guess))