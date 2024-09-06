"""def factorial(n):
    if  n == 0 and n == 1:
        return 1
    else:
        return n * factorial(n - 1)
number = 5
print(f"Factorial of {number} is {factorial(number)}")
"""
"""def factorial(n):
    result = 1
    for i in range(2,n + 1):
        result *= i
    return result
print(f"factorial of given number is {factorial(5)}")
"""
import math
def factorial(n):
    return math.factorial(n)
number = int(input("enter a number: "))
print(f"factorial of {number}is{factorial(number)}")
    
    
    


