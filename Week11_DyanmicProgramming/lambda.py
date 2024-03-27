# Function that takes in a number and returns the square of it
'''def square_num(a):
    return a*a
print(square_num(5))

square_num1 =  lambda x: x * x
print(square_num1(5))

hello = lambda x: f"Hello {x}"
print(hello('Jane'))

# Write a lambda function that checks whether a number is even or not
check_evcen = lambda num: "Even Number" if num % 2 == 0 else "Odd Number"
print(check_even(17))

print((lambda x: f"Hello {x}")('Ryan'))
# Immediately Invoked Function Expressions or IIFEs
print((lambda x: x * x)(2))

add_nums = lambda x, y: x+y
print(add_nums(2, 3))
'''

# Higher Order Functions --> filter, map, reduce
nums = [3, 2, 6, 8, 4, 6, 2, 9]
# Filter
def is_even(n):
    return n % 2 == 0

even_nums = filter(is_even, nums)
print(list(even_nums))

even_nums1 = filter(lambda n: n % 2 == 0, nums)
print(list(even_nums1))

# Map
def update_num(n):
    return n * 2

doubles = map(lambda n: n * 2, nums)
print(list(doubles))

cities = ['Boston', 'New York', 'Miami', 'Los Angeles', 'Phoenix']
# Using amp and lmabda, return a list with the length of each string in cities
cities_length = map(lambda x: len(x), cities)
print(list(cities_length))

# Reduce --> used to reduce a given list to a single number
from functools import reduce

def add_all(a, b):
    return a + b
sum_value = reduce(add_all, nums)
print(sum_value)

sum_value1 = reduce(lambda a,b: a + b, nums)
print(sum_value1)

