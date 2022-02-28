current_price = int(input()) #Get current and last month prices
lm_price = int(input())
monthly_mor = (current_price * 0.051) / 12 #Formula for monthly mortgage



''' Type your code here. '''

print(f'This house is ${current_price}. The change is ${current_price - lm_price} since last month.')
print(f'The estimated monthly mortgage is ${monthly_mor:.2f}.')