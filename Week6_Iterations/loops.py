'''
x = 1

while x < 5:
    print(x)
    x += 1
    #x = x + 1 - Top is shorthand

## Print first 10 natural numbers (Start from 1)
x = 1

while x <= 10:
    print(x)
    x += 1

## Break
x = 1
while x <= 10:
    if x == 5:
        #break # Break is conditional and the number that equals to it doesn't show but the numbers before it does
        print('Found 5!')
        #ontinue # Will skip the next lines and continue with next iteration once if condition is satisfied
    print(x)
    x += 1

## For loops
nums = [1, 2, 3, 4, 5]
for num in nums:
    print(num + 2)
    if num == 3:
        break

## Range function
for i in range(10):
    print(i)

## Sum of first 100 numbers
sum = 0
for i in range(101):
    sum = sum + i
    print(sum)

## Multiplication table (upto 10) for a given num
num = int(input('Enter a number: '))

for i in range(1, 11, 2): # range(start, stop, step)
    print(f'{num}*{i}: ', num*i)

## Reverse
for i in range(-10, -0):
    print(i)

## Nested Loops
nums = [1, 2, 3, 4, 5]
for num in nums:
    for letter in 'abc':
        print(num, letter)

for letter in 'abcde':
    print(letter)
'''
rows = int(input('Enter the number of rows: '))
for i in range(1, rows+1):
    for j in range(1, i+1):
        print(j, end=' ')
    print()
