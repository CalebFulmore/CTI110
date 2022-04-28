# CTI-110
# P4HW2 - Pizza Order
# Caleb Fulmore
# 4/7/2022
#
# Get number of students 
# Get number of students per pizza
# If value for number of students is incorrect, give error message and restart
# Calculate price of pizzas needed
# Display number of students, pizzas needed, and price
# Ask user if they want to run the program again
# Pending their response, restart the program or terminate
#

import math

    
while True:
    num_students = int(input('How many students do you want to order pizza for? '))
    num_per_pizza = float(input('Enter number of students per pizza(1.5, 2, 3)?: '))
    if num_per_pizza != 2 and num_per_pizza != 1.5 and num_per_pizza != 3:
        print('INVALID ENTRY!!!!\nShould have entered 1.5, 2, or 3')
        num_per_pizza = float(input('Enter number of students per pizza again. (1.5, 2, 3): '))
        continue
    else:
        pizzas_needed = math.ceil(num_students / num_per_pizza)
        print('----Pizza Ordered-------')
        print('Number of Students :', num_students)
        print('Pizzas Needed :', pizzas_needed)
        price = (pizzas_needed * 5) * 1.06
        print('Price $''%.2f' %price)
        print('---------------------')
        answer = str(input('Would you like to run program again? (y for yes) '))
        if answer == 'y':
            continue
        if answer == 'n':
            break
print('Program Terminated')
