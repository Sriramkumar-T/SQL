def calc(x,y):
    p=1
    for i in range(1,y+1):
        p=p*x
    return p
n=int(input())
p=int(input())
print(calc(n,p))
