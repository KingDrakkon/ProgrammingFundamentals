'''
for i in range(11):
    if i >= 5: # if i > 5: this makes it from 0 - 5
        break
    else:
        print(i)
# Will print from 0 to 4

for i in range(11):
    if i % 2 == 0:
        continue
    else:
        print(i)

Write a program to calculate the sum and average of digits p[resent in a string
Ex: random289$18@str849ing6

total = 0
count = 0

input_str = input('Enter a string with digits and other characters: ')
for char in input_str:
    # print(char)
    if char.isdigit():
        total = total + int(char)
        count = count + 1
print(round(total, 2))
print(round(total/count), 2)
'''
digits = 0
letters = 0
symbols = 0

input_str = input('Enter a string with digits and other characters: ')
for char in input_str:
    if char.isdigit():
        digits = digits + 1
    elif char.isalpha():
        letters = letters + 1
    else:
        symbols = symbols + 1
print(['Digits', digits], ['Letters', letters], ['Symbols', symbols])
'''
If - Else: Just One Condition

If - Elif - Else: Multiple Conditions

= vs ==: First = means x = # and == means something equals it

F strings

Dictionaries
Iterating → dict.keys(), dict.values(), dict.items()
	For value in dict.values():
Use the value for other operations

Creating empty collections(lists, sets, dictionaries)

String to list conversions, list to string conversion

Creating a set out of a list or a string

While Loop (Pt. 1)
X = 1
While x < 10:
Add a break to stop loop
X = x + 1 is to keep increasing the number within the loop
Iteration

For Loop (Pt. 2)
For x in range (11)
print(2)
More compressed version of While loop
Repetition

Break, Continue
	Break: Stops the loop until meant number

Random module - RPS Game

List Functions - length, pop, remove, append, insert, extend

Set Functions - union, intersection, difference

Pattern Problems:
1
1	2
1	2	3
1	2
1
'''

