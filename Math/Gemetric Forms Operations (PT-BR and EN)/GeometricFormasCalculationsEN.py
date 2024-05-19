# Date: 05/19/2024
# Activity: Create an program with the specifications:
#   1 - The user can select one of the options:
#           - Circle
#           - Retangle
#           - Triangle
#           - Square
#   2 - By the selected option, the user need enter this information:
#           - For Circle > radius
#           - For Retangle > Base and hight
#           - For Triangle > Base, hight and side
#           - For Square > Side
#   3 - The program need calculate: 
#           - For Circle > Area, diameter and circuference
#           - For Retangle > Area and perimeter
#           - For Triangle > Area and perimeter
#           - For Square > Area and perimeter
# Author: Higor Stanley aka Devyat009

import math;
# Function.
# itsaNumber? function to validate user input, it trown false in wrong input.
def itsaNumber(string):
    try:
        if string.isnumeric():
            format_int = int(string)
            return True
        else:
            format_float = float(string)
            return True
    except ValueError:
        return False
# Program in state of loop.   
while True:
        decision = (input('''Choose one of these options:
                        [1] Circle
                        [2] Retangle
                        [3] Triangle
                        [4] Square
                        [5] Leave
                        Option to be chosen: '''))
    # Validates if the user input is an valid number.
        if itsaNumber(decision):
            # Decision 1: Circle
            if decision == '1':
                while True:
                    radius = input('Enter the radios of the circle: ')
                    if itsaNumber(radius):
                        radius = float(radius)
                        circuference = (2 * math.pi) * radius
                        area = math.pi * (radius ** 2)
                        diameter = 2 * radius 
                        print(f'''The result of math operations for the circle with the {radius} is:\n
                            Circuference: {circuference}
                            Area: {area}
                            Diameter: {diameter}''')
                        break
                    else:
                        print('\nEnter an valid number for the radius!\n')    
            # Decision 2: Retangle
            elif decision == '2':
                while True:
                    hight = input('Enter the hight size of the retangle: ')
                    if itsaNumber(hight):
                        hight = float(hight)
                        while True:
                            base = input('Enter the base size of the retangle: ')
                            if itsaNumber(base):
                                base = float(base)
                                area = hight * base
                                perimeter = 2 * (base + hight)
                                print(f'''The result of math operations of an retangle using {hight} as hight and {base} for the base:\n
                                        Area: {area}
                                        Perimeter: {perimeter}''')
                                break
                            else:
                                print('\nEnter an valid number for the base!\n')
                        break    
                    else:
                        print('\nEnter an valid number for the hight!\n')
            # Decision 3: Triangle
            # Multi 'while' for every inserted input by user to validate if is correct, using the 'itsaNumber' function
            elif decision == '3':
                while True:
                    hight = input('Enter the hight size of the triangle: ')
                    if itsaNumber(hight):
                        hight = float(hight)
                        while True:
                            base = input('Enter the base size of the triangle: ')
                            if itsaNumber(base):
                                base = float(base)
                                while True:
                                    side = input('Enter the side size of the triangle: ')
                                    if itsaNumber(side):
                                        side = float(side)
                                        area = 1/2 * (base * hight)
                                        perimeter = base + side + side
                                        print(f'''The result of math operations of an retangle using {hight} as hight and {base} for the base and {side} for the side:\n
                                                    Area: {area}
                                                    Perimeter: {perimeter}''')
                                        break
                                    else:
                                        print('\nEnter an valid number for the side!\n')
                                break
                            else:
                                print('\nEnter an valid number for the base!\n')
                        break
                    else:
                        print('\nEnter an valid number for the hight!\n')
            # Decision 4: Square
            elif decision == '4':
                while True:
                    side = input('Enter the side size of the square: ')
                    if itsaNumber(side):
                        area = side ** 2
                        perimeter = side + side + side + side
                        print(f'''The result of math operatins of an square using {side} side size:\n
                                Area: {area}
                                Perimeter: {perimeter}''')
                        break
                    else:
                        print('\nEnter an valid number for the side!\n')
            # Decision 5: Leave the program
            elif decision == '5':
                print('Leaving...')
                break
            # Outer scope option  
            else:
                print('\nInvanlid option detected, try again\n')
        # IF user input be an non valid decision alert
        else: 
            print('\nEnter a number between 1 and 5!!\n')
