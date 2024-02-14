'''
Take an input value for n

print out the numbers from 1 to n with the below conditions for each number
1. If num is divisible by 3 --> print 'Fizz'
2. If num is divisible by 5 --> print 'Buzz'
3. If num is divisible by 3 and 5 --> print 'FizzBuzz'
If none of the above conditions are satisfied, just print the number
'''

target_num = int(input('Enter a target number: '))

for num in range(1, target_num + 1):
    if num % 3 == 0 and num % 5 == 0:
        print('FizzBuzz')
    elif num % 3 == 0:
        print('Fizz')
    elif num % 5 == 0:
        print('Buzz')
    else:
        print(num)
