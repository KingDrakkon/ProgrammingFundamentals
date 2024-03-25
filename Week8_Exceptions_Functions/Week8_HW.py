'''
# Question 1: Write a function to check whether a given string or number is palindrome or not
# from typing import List
def checkPalindrome(str1):
    if str1 == str1[::-1]:
        result = True
    else:
        result = False

    #print(result) this is for is I dont want to type print("True/False")
    return result

str1 = input('Enter a word: ') #eye
isPalindrome = checkPalindrome(str1)
print(isPalindrome)# This is for if I am just returning the result from a previous check

# Question 2: Write a function to check whether a given is string is anagram or not
str1 = sorted(input('Enter a word: '))
str2 = sorted(input('Enter the same word different order: '))

def checkAnagram(str1, str2):
    result = ''
    if str1 == str2:
        result = True
        print('True')
    else:
        result = False
        print('False')
    return result
isAnagram = checkAnagram(str1, str2)

# Question 3: Write a function to that takes user name, birth year, budget, price of the product as
# inputs and performs the following operations.
str1 = input('Enter a name: ')
str2 = input('Enter your birthyear: ')
print(type(str2))
str3 = input('Enter your budget: ')
str4 = input('Enter price of product: ')

num = 2024
result = num - int(str2)# int command turning input string into an integer

how_much = int(str3) // int(str4)# Error if budget is 0


print('User Info', (str1, str2, str3, str4))
print(f"Hello {str1}! You are {result} years old and you can buy {how_much}.")
'''

str1 = int(input('Enter a side: '))
str2 = int(input('Enter a side: '))
str3 = int(input('Enter a side: '))


