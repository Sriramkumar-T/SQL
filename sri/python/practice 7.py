"""year=int(input("enter a year"))
if(year%4==0):
    print("it is a leap year")
else:
    print("it is not a leap year")
    """
# prime numbers
"""def prime_number(n):
    if n<=1:
        return False
    if n==2:
        return True
    if n%2==0:
        return False
    divisor = int(n**0.5)+1
    for i in range(3,divisor,2):
        if n%i == 0:
            return False
    return True
def prime_series(series):
    return[num for num in series if prime_number(num)]
series = range(10,50)
prime = prime_series(series)
print(prime)"""
#count numbers in digits
"""def count_digit_occurrences(n, d):
    # Convert the number to a string
    n_str = str(n)
    # Convert the digit to a string
    d_str = str(d)
    # Count the occurrences of the digit in the number
    return n_str.count(d_str)

# Example usage:
n = int(input("enter a numbers:"))
d = int(input("enter a number to find:"))
result = count_digit_occurrences(n, d)
print(f"The digit {d} appears {result} times in the number {n}.")
"""
#pattern1

"""n = 5                                  
for i in range(1,n+1):                     
        print(" "*n+"*"*i)  
 n = 5
for i in range(1,n+1):
        print(""*(n-i)+"*"*i)                   
"""
#pattern2
"""n=5                                       
for i in range(n,0,-1):                    
    print(""*n+"*"*i)
"""
#patern3
"""n= 5
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end=" ")
    
    print()
n=5
for i in range(n,0,-1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
n=5
for i in range(1, n+1):
    print(" "*(n-i),end=" ")
    print("* "*i)

n=5
for i in range(1,n+1):
    print(" "*(n-i),end=" ")
    print("* "*i)
for i in range(n,0,-1):
    print(" "*(n-i),end=" ")
    print("* "*i)
n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
n=5 
for i in range(n,0,-1):
    for j in range(i,0,-1):
        print(j,end=" ")
    print()"""
n=5 
for i in range(1):
    print("*"*(n)+"    "+"*    "*(n-3))
    print("*    "*(n-3)+"    "+"*  "*(n-3))
    print("*    "*(n-3)+"    "+"* "*(n-3))
    print("*"*(n)+"    "+"*")
    print("*    "*(n-3)+"    "+"* "*(n-3))
    print("*    "*(n-3)+"    "+"*  "*(n-3))
    print("*"*(n)+"    "+"*    "*(n-3))
print()
print("        ")
n=5
for i in range(1):
    print("*    "*(n-3))
    print("*   "*(n-3))
    print("*  "*(n-3))
    print("* "*(n-3) )
    print("*")
    print("* "*(n-3))
    print("*  "*(n-3))
    print("*   "*(n-3))
    print("*    "*(n-3))
    
