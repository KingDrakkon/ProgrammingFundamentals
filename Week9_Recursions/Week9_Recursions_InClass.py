def findFactorial(num):
    if (num <= 1):
        return 1
    else:
        return num * findFactorial(num - 1)

factorial_value = findFactorial(5)
print(factorial_value)
