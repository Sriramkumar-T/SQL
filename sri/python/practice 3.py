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
"""import math
def factorial(n):
    return math.factorial(n)
number = int(input("enter a number: "))
print(f"factorial of {number}is{factorial(number)}")
print()"""
#prime number
"""n=int(input("enter a prime number:"))
if n>1 :
    for i in range(2,n):
        if(n%i)==0:
            print("the given number is not a prime number")
            break
    else:
        print("the given number is prime number")
else:
    print("enter a nu,ber greater than one")   """  
#prime number in series    
start=int(input("enter a starting number:"))
end=int(input("enter a end number:"))
print("the prime numbers from",start,"to",end,":")
if(start>1):
    for i in range(start,end+1):
        flag=0
        for j in range(2,i):
            if(i%j==0):
                flag=1
                break
        if(flag==0):
            print(i,end=" ")
print()
    


