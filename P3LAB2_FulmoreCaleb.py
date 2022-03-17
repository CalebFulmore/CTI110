#ask customer what service they want
desired_service = input('Enter desired auto service:\n')

#inform customer of price
if desired_service == 'Oil change':
    print('You entered:', desired_service)
    print('Cost of oil change: $35')

elif desired_service == 'Tire rotation':
    print('You entered:', desired_service)
    print('Cost of tire rotation: $19')

elif desired_service == 'Car wash':
    print('You entered:', desired_service)
    print('Cost of car wash: $7')

#give error message for false requests
else:
    print('You entered:', desired_service)
    print('Error: Requested service is not recognized')

