 # Math Quiz for addition and subtraction of random numbers
 # 4/28/2022
 # CTI-110 P5HW2 - Math Quiz
 # Caleb Fulmore
 #
 # Main menu gives three options
 # Option 1 generates 2 random numbers to add together
 # Display math problem to user
 # Get user input
 # congratulate if input is correct
 # tell user how many attempts they took
 # if answer is wrong, tell if too high or low
 # return to main menu
 # Option 2 does same except with subtraction
 # Option 3 terminates program
 #

import random

def addition():
    num1=random.randint(0,999)
    num2=random.randint(0,999)
    guesses = 1
    print(' '+str(num1));
    print('+'+str(num2));
    answer = int(input());
    while answer != (num1 + num2):
        guesses = guesses + 1
        if answer < (num1+num2):
            print('Sorry, guess was too low.')
        else:
            print('Sorry, guess was too high.')
        answer = int(input("try again : "))
    print('Congratlations!!!! Your answer is correct...')
    print('You got it on guess number',guesses,'Great job!')
def subtraction():
    num1=random.randint(0,999)
    num2=random.randint(0,999)
    guesses = 1
    print(' '+str(num1));
    print('-'+str(num2));
    answer = int(input());
    while answer != (num1 - num2):
        guesses = guesses + 1
        if answer < (num1-num2):
            print('Sorry, guess was too low.')
        else:
            print('Sorry, guess was too high.')
        answer = int(input("try again : "))
    print('Congratlations!!!! Your answer is correct...')
    print('You got it on guess number',guesses,'Great job!')
    
def main():
    print('Welcome to Math Quiz')
    print(' ')
    while True:
        print('MAIN MENU')
        print('--------------------')
        print('1. Adding Random Numbers')
        print('2. Subtracting Random Numbers')
        print('3. Exit')
        choice = input('Please choose one of the menu options: ')
        if choice == '1':
            addition()
        elif choice == '2':
            subtraction()
        elif choice == '3':
            print('Thank you for playing')
            print('Bye!!')
            break
        elif choice != '1' or '2' or '3':
            print('error')
            main()
main()
        
