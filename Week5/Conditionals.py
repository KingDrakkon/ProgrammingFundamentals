'''
height = int(input('Please enter your height in cms: '))

if height > 120:
    print('Can ride')
else:
    print('Can\'t ride')


# Nested if-else
height = int(input('Please enter your height in cms: '))

if height > 120:
    print('Can ride')
    age = int(input('Enter your age: '))
    if age > 18:
        print('Ticket is $12')
    else:
        print('Ticket is $7')
else:
    print('Can\'t ride')


height = int(input('Please enter your height in cms: '))
bill = 0

if height > 120:
    print('Can ride')
    age = int(input('Enter your age: '))
    if age < 12:
        ticket_price = 5
        print('Ticket is $5')
    elif age >=12 and age < 18:
        ticket_price = 7
        print('Ticket is $7')
    else:
        ticket_price = 12
        print('Ticket is $12')
    want_photos = input('Do you want a photo taken? Enter Y/y or N/n: ')

    if want_photos == "Y" or want_photos == "y":
        bill = ticket_price + 3

    print(f'Your final bill is ${bill}')
else:
    print('Can\'t ride')


height = int(input('Please enter your height in cms: '))
bill = 0

if height > 120:
    print('Can ride')
    age = int(input('Enter your age: '))
    if age < 12:
        ticket_price = 5
        print('Ticket is $5')
    elif age >= 12 and age < 18:
        ticket_price = 7
        print('Ticket is $7')
    elif age >= 18 and age < 45:
        ticket_price = 12
        print('Ticket is $12')
    else:
        ticket_price = 0
        print('Ticker is $0')
    want_photos = input('Do you want a photo taken? Enter Y/y or N/n: ')

    if want_photos == "Y" or want_photos == "y":
        bill = ticket_price + 3

    print(f'Your final bill is ${bill}')
else:
    print('Can\'t ride')
'''

grade = int(input('Please enter your number grade: '))

if grade < 60:
    print('F')

elif grade < 70:
    if grade < 63:
        print('D-')
    elif grade >=63 and grade < 67:
        print('D')
    else:
        print('D+')

elif grade < 80:
    if grade < 73:
        print('C-')
    elif grade >=73 and grade < 77:
        print('C')
    else:
        print('C+')

elif grade < 90:
    if grade < 83:
        print('B-')
    elif grade >=83 and grade < 87:
        print('B')
    else:
        print('B+')

elif grade < 100:
    if grade < 93:
        print('A-')
    elif grade >=93 and grade < 97:
        print('A')
    else:
        print('A+')
