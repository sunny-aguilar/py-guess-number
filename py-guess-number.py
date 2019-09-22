# Guess the number game

# import random module
import random

# main function
def main():
    # create a random number
    number = random.randint(1, 100)

    # flag value
    guess = True

    # keep playing game at user's request
    while guess:
        my_guess = input('Enter the number I am thinking of: ')
        if my_guess == number:
            print('Eureka! You guessed correct!')
        elif my_guess < number:
            print('Your guess was too low, try again.')
        elif my_guess > number:
            print('Your guess was too high, guess again.')


        guess = input('Would you like to guess again? (Y/N) ')
        if guess.upper == 'Y':
            guess = True
        else:
            guess = False

# call main function
main()
