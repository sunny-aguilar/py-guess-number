# Guess the number game using random module

# import random module
import random

# main function
def main():
    # create a random number to be guessed
    number = random.randint(1, 1000)

    # boolean flag
    guess = True

    # keep playing game at user's request
    while guess:
        # get user's guess and convert to integer
        my_guess = int(input('Enter the number I am thinking of: '))

        # compare user's guess to right number
        if my_guess == number:
            print('Eureka! You guessed correct!')
            guess = False
        elif my_guess < number:
            print('Your guess was too low, try again.')
        elif my_guess > number:
            print('Your guess was too high, guess again.')

# call main function to start game
main()
