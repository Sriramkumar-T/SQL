n=int(input())
digit=0
while(n!=0):
    n//=10
    digit+=1
print(digit)
