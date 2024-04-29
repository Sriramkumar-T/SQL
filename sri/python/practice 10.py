def prime(x,y):
    plist=[]
    for i in range(x,y):
        if i==0 or i==1:
            continue
        else:
            for j in range(2,int(i/2)+1):
                if i%j ==0:
                    break
                else:
                    plist.append(i)
    return plist
s=int(input("starting range:"))
p=int(input("ending range:"))
lst=prime(s,p)
if len(lst)==0:
    print("there are  no prime num")
else:
    print("the prime numbers are",lst)
