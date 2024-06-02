# Author: Higor Stanley aka Devyat009
# Guess The Number

import random

# Validete if is a integer number:
def itsanumber(string):
    if string.isnumeric():
        return True
    else:
        return False

# Coming soon
#def customMode:

while True:
    userChoice = input('''Choose the dificulty: 
                [1] Normal
                [2] Hard
                [3] Impossible
                [4] Custom
                [5] Exit
                Your choice is: ''')
    if itsanumber(userChoice):
        userChoice = int(userChoice)
        if userChoice == 1:
            print('\nThe computer selected a number betwen 1 and 10. You have unlimited guess in normal dificulty.\nBut every wrong guess the computer will choose another number...')
            while True:
                userInput = input('What is your guess? Insert a number: ')
                if itsanumber(userInput):
                    userInput = int(userInput)
                    syschoice = random.randint(1,10)
                    if userInput == syschoice:
                        print(f'\nYou guessed correctly, the computer chose {syschoice}\n')
                        break
                    elif userInput < 1 or userInput > 10:
                        print('Choose a number between 1 and 10, and try again.')
                    else:
                        print('Wrong guess, try again.')
                else:
                    print('Invalid input, please use numbers')
            break # If let this break, will break when guessed correctly
        elif userChoice == 2:
            print('The computer selected a number between 1 and 15. You have 4 chances to guess.')
            syschoice = random.randint(1, 15)
            for i in range(4):
                userInput = input('What is your guess? Insert a number: ')
                if itsanumber(userInput):
                    userInput = int(userInput)
                    if userInput == syschoice:
                        print(f'\nYou guessed correctly, the computer chose {syschoice}\n')
                        break
                    elif userInput < 1 or userInput > 15:
                        print('Choose a number between 1 and 15, and try again.')
                    else:
                        print('Wrong guess, try again.')
                else:
                    print('Invalid input, please use numbers')
            else:
                print(f'Sorry, you\'ve used all your chances. The correct number was {syschoice}.')
            break
        elif userChoice == 3:
            print('Coming soon...')
            break
        #     # Implement the logic for 'Impossible' difficulty
        elif userChoice == 4:
            print('Coming soon too...')
            break
        #     # Implement the logic for 'Custom' difficulty
        elif userChoice == 5:
            print('Exiting...')
            break
        else:
            print('Invalid choice, please choose from 1 to 5')
    else:
        print('Please insert a number between 1 and 5')