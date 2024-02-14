'''
# How do change in from number form to letter form
list1 = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

num = int(input('Enter a digit between 0 and 9: '))

print(list1[num])

dict1 = {
    0: 'zero',
    1: 'one',
    2: 'two'
}

print(dict1.get(num))

## Question 2: Rock Paper Scissors
# How to play rock paper scissors
import random
# rand_num = random.random() #Generates a random value between 0 and 1
# print(round(rand_num,2))
user_choice = 'yes'
while user_choice.lower() == 'yes':
    user_move = input('Pick a move - rock/paper/scissors: ')
    rand_num = round(random.random(), 2)
    comp_move = ''

    if rand_num >= 0 and rand_num < 1/3:
        comp_move = 'rock'
    elif rand_num >= 1/3 and rand_num <2/3:
        comp_move = 'paper'
    else:
        comp_move = 'scissors'

    result = ''

    if user_move == comp_move:
        result = 'Tie.'
    elif user_move == 'rock':
        if comp_move == 'paper':
            result = 'You lose!'
        else:
            result = 'You Win!'
    elif user_move == 'paper':
        if comp_move == 'scissors':
            result = 'You lose!'
        else:
            result = 'You Win!'
    elif user_move == 'scissors':
        if comp_move == 'rock':
            result = 'You lose!'
        else:
            result = 'You Win!'

    print(f'You picked {user_move}. Computer picked {comp_move}. {result}')
    user_choice = input('Do you want to continue? Enter yes or no: ')

print('Thank you!')

# Quesion 3:
# How to have long term division
year = int(input('Type a year: '))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print('Leap Year')
        else:
            print('Not Leap Year')
    else:
        print('Leap Year')
else:
    print('Not Leap Year')
'''
# Question 4:
#print('Welcome to Treasure Island. Your mission to find the treasure.')
treasure = input("Left or Right?: ")
if treasure == 'Right':
    print("Good Job!")
    treasure = input("Would you like to Swim or Wait?: ")
    if treasure == 'Wait':
        print('Good Job!: ')
        treasure = input("Which door will you choose?: ")
        if treasure == 'Red':
            print('Burned by fire. Gamer over.')
        elif treasure == 'Yellow':
            print('You Win!')
        elif treasure == 'Blue':
            print('Eaten by beasts. Gamer Over.')
        else:
            print('Gamer Over.')
    else:
        print('Attacked by trout. Game Over')
else:
    print("Fall into a hole. Game over")

