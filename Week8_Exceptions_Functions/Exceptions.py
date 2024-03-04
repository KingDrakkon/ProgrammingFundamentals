'''
## Normal Statement
a = 5
b = 0
## Critical Statement
try:
    print(a/b)
except:
    print('Cannot divide by zero.')
print('Bye')

try:
    a = int(input('Enter first number: '))
    b = int(input('Enter second number: '))
    result = a / b
    print('Connection Opened')
except ZeroDivisionError as e:
    print('Something went wrong. ', e)
except ValueError as e:
    print('Soemthing went wrong', e)
except Exception as e:
    print(e)
else:
    print(result)
finally:
    print('Connection Closed')

print('End')
'''

numbers = [1, 2, 3, 0, 4, 5]
for num in numbers:
    try:
        result = 10/num
    except ZeroDivisionError as e:
        print('Cannot divide by Zero.')
    except Exception as e:
        print('Something went wrong. ', e)
    else:
        print(result)
