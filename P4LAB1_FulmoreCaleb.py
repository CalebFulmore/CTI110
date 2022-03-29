user_text = input()
uncounted = ' ,.!'
count = 0
for characters in user_text:
    if characters not in uncounted:
        count += 1
print(count)
