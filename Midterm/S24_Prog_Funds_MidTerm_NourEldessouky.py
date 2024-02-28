'''
# QUESTION 1: Coin-Toss Game
import random
user_choice = 'yes'
while user_choice.lower() == 'yes':
    user_move = input('Pick a side - Heads or Tails: ')
    rand_num = round(random.random(), 2)
    comp_move = ''

    if rand_num >= 0 and rand_num < 1/2:
        comp_move = 'heads'
    else:
        comp_move = 'tails'

    result = ''

    if user_move == comp_move:
        result = 'Tie.'
    elif user_move == 'heads':
        if comp_move == 'tails':
            result = 'You Wim!'
        else:
            result = 'You Win!'
    elif user_move == 'tails':
        if comp_move == 'heads':
            result = 'You lose!'
        else:
            result = 'You Win!'
    elif user_move == 'tails':
        if comp_move == 'tails':
            result = 'Tie!'
        else:
            result = 'You Win!'
    elif user_move == 'heads':
        if comp_move == 'heads':
            result = 'Tie!'
        else:
            result = 'You Win'

    print(f'You picked {user_move}. Computer picked {comp_move}. {result}')
    user_choice = input('Do you want to continue? Enter yes or no: ')

print('Thank you!')

# QUESTION 2: Multiples of 5
list1 = [12, 75, 150, 180, 145, 525, 50]

for num in list1:
    if num % 5 == 0:
        print(num)
    elif num <= 150:
        continue
    elif num < 500:
        break
    else:
        print()

# QUESTION 3: Pattern depending on rows
rows = int(input('Enter any number of rows: '))
for i in range(0, rows):
    for j in range(0, i + 1):
        print(j*2, end=' ')
    print()
'''
# QUESTION 4: Factors
target_num = int(input('Enter a number: '))

if num % 1 == 0 and num % num == 0:


