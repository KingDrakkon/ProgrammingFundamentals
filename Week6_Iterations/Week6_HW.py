'''
# Question 1: Write a program to print a list of all prime numbers till a given target number.
target_num = int(input('Enter a number: '))
prime_list = []

if target_num <= 1:
    print('Enter a number greater than 1')
elif target_num == 2:
    prime_list.append(target_num)
    print(prime_list)
else:
    for num in range(2, target_num):
        isPrime = True
        for i in range(2, num):
            if num % i == 0:
                isPrime = False
                break
        if isPrime is True:
            prime_list.append(num)
    print(prime_list)

# Question 2: Write a program to print a list of all even numbers till a given target number.
target_num = int(input('Enter a number: '))
list1 = [0, 2, 4, 6, 8, 10]

for num in list1:
    if num % 2 == 0:
        print(num, end=" ")

# Question 3: Use a loop to display elements from a given list present at odd index positions.
list1 = [1, 2, 3, 4, 5];

print("Elements of given array present on odd position: ");
# Loop through the array by incrementing the value of i by 2

for i in range(0, len(list1), 2):
    print(list1[i]);
'''
# Question 4: Find the highest number from a given list of numbers using for loop. Do not use any
# in-built functions
def myMax(list1):
    max = list1[0]
    for x in list1:
        if x > max:
            max = x
    return max
list1 = [10, 20, 4, 45, 99]
print("Largest element is:", myMax(list1))
