# A program that calculates sales tax and total price of purchased items
# 3-1-2022
# CTI-110 P2HW1 - Total Purchases
# Caleb Fulmore
#
# Get prices of each item from user
# Program calculates subtotal through addition
# Program calculates taxes through multiplication
# Program calculates total by adding taxes to the subtotal
#   Program limits taxes, total, and subtotal to 2 decimal places like money
#




num1 = float(input("Enter the price of item#1: "))
num2 = float(input("Enter the price of item#2: "))
num3 = float(input("Enter the price of item#3: "))
num4 = float(input("Enter the price of item#4: "))
num5 = float(input("Enter the price of item#5: "))

subtotal = num1 + num2 + num3 + num4 + num5
format_subtotal = "{:.2f}".format(subtotal)
tax = subtotal * .07
format_tax = "{:.2f}".format(tax)
total = subtotal + tax
format_total = "{:.2f}".format(total)

print('-------Results-------')
print('Subtotal: ', format_subtotal)
print('Sales Tax: ', format_tax)
print('Total: ', format_total)


