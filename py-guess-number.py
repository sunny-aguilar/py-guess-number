# Guess the number game

# import random module
import random

# create a random number
number = random.randint(1, 100)

# flag value
guess = True

# keep playing game at user's request
while guess:
    print('Guess the number I am thinking of: ')
    guess = input('Would you like to guess again? (Y/N) ')
    if guess.upper == 'Y':
        guess = True
    else:
        guess = False
        
