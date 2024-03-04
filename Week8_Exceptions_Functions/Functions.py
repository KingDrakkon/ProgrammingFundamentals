'''
Functions - to resuse code

# num --> function parameter
def checkEven(num):
    result = ''
    if num % 2 == 0:
        result = True
    else:
        result = True
    return result

## Making a function call
isEven = checkEven(4)
print(isEven)
#isEven = checkEven(9)

print('Hello') # print function has no return target
import random
randNum = random.random() # random funtion returns a number
'''

def checkAnagram(letter):
    result = ''
    if letter == letter:
        result = True
    else:
        result = False
    return result

word = int(input('Enter a word: '))
print(word)
word = int(input('Enter a word in different order: '))
print(word)
isAnagram = checkAnagram()