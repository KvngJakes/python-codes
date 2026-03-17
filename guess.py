'''
secret_number= 7
    guess = 0
    while True:
        guess = secret_number
        guess = int(input("Guess the number between 1 and 10: "))
        if guess < secret_number:
            print("Too low!, Try Again")
        elif guess > secret_number:
            print("Too High! Try Again")
        else:
            print("Congratulation, You guessed right")
'''


