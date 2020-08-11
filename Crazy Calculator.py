'''
This program was developed by CreeperDoolie as a tool for calculation of addition, 
subtraction, multiplication, and division in a command line for two integers.
'''

import time

'''intro panel'''
print('---------------------------------------------------------')
print('                    Crazy Calculator!                    ')
print('                    By: CreeperDoolie                    ')
print('---------------------------------------------------------')

print('')

'''asks for a specific operator and verifies if valid'''
def calculator():
    while True: 
        operator = input('Enter an operator (+,-,*,/): ')
        if operator == '+':
            print('')
            break
        elif operator == '-':
            print('')
            break
        elif operator == '*':
            print('')
            break
        elif operator == '/':
            print('')
            break
        else:
            print('')
            print('Invalid operator. Please try again')
            print('')

    '''asks for two numbers'''
    number1 = int(input('Enter your first number: '))
    print('')
    number2 = int(input('Enter your second number: '))
    print('')

    '''if cases for each operator''' 
    if operator == '+':
        print('{} + {} = '.format(number1, number2), end='')
        print(number1 + number2)
        print('')
        time.sleep(5)
    elif operator == '-':
        print('{} - {} = '.format(number1, number2), end='')
        print(number1 - number2)
        print('')
        time.sleep(5)
    elif operator == '*':
        print('{} * {} = '.format(number1, number2), end='')
        print(number1 * number2)
        print('')
        time.sleep(5)
    elif operator == '/':
        print('{} / {} = '.format(number1, number2), end='')
        print(number1 / number2)
        print('')
        time.sleep(5)
    else:
        print('Uh Oh. Something happened to cause the calculator to fail. It wasnt you...(maybe) Please input your equation again.')
        print('')
        calculator()
calculator()

'''asks if user wants to input another equation and if cases for yes or no input'''
while True:
    cont = input('Would you like to enter another equation? (y/n): ')    
    if cont == 'y':
        print('')
        calculator()
    elif cont == 'n':
        print('')
        print('Thank you for using Crazy Calculator!')
        time.sleep(3)
        break
    else:
        print('')
        print('That is not a valid response, plese enter one of the following (y/n)')
        print('')