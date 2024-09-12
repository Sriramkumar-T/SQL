
#patter A

for i in range(7):
    for j in range(6):
        if((j==0 or j==4 ) and i!=0) or ((i==0 or i==3)and (j>0 and j<4)):
            print("*",end="")
        else:
            print(end=" ")
    print()
print()
#pattern B

for i in range(7):
    for j in range(6): 
        if((j==0 )or (j==4 and i!=0 and i!=3 and i!=6)) or ((i==0 or i==3 or i==6) and (j>0 and j<4)):
            print("*",end="")
        else:
            print(end=" ")
    print()
print()
#pattern C

for i in range(7):
    for j in range(6):
        if(j==0 and (i!=0 and i!=6) )or((i==0 or i==6)and(j>0)):
            print("*",end="")
        else:
            print(end=" ")
    print()
print()

#patter D

for i in range(7):
    for j in range(6):
        if(j==0 or (j==5 and (i!=0 and i!=6))) or ((i==0 or i==6)and(j>0 and j<5)) :
            print("*",end="")
        else:
            print(end=" ")

    print()
print()

#pattern E
for i in range(7):
    for j in range(6):
        if(j==0  ) or ((i==0 or i==3 or i==6)and(j>0)): 
            print("*",end="")
        else:
            print(end="")
    print()
print()

#pattern F

for i in range(7):
    for j in range(6):
        if(j==0 and i!=2) or ((i==0 or i==2)and(j>0)):
            print("*",end="")
        else:
            print(end="")
    print()
print()

#pattern G
for i in range(7):
    for j in range(6):
        if((j==0 and i!=0) or (j==4 and i!=2 and i!=3 )) or ((i==0 or i==6)and (j>0 and j<4)) or (j==3 and i==4):
            print("*",end="")
        else:
            print(end=" ")
    print()
print()

#pattern H
for i in range(7):
    for j in range(6):
        if(j==0 or j==4)or((i==3) and (j>0 and j<4)):
            print("*",end="")
        else:
            print(end=" ")
    print()
print()

#pattern I
for i in range(7):
    for j in range(6):
        if(j==2)or(i==0 or i==6):
            print("*",end="")
        else:
            print(end=" ")
    print()
print()

# pattern J
for i in range(7):
    for j in range(6):
        if((j==0)and( i!=1 and i!=2 and i!=3 and i!=4 and i!=6) or (j==3)) or (( i==0 or i==6)and(j<4)):
            print("*",end="")
        else:
            print(end=" ")
    print()
print()

# pattern k
a=0
b=4
for i in range(7):
    for j in range(6):
        if(j==0)or (i+j==3 or i-j==2):
            print("*",end="")
        
        else:
            print(end=" ")

    print()
print()

#pattern L
for i in range(7):
    for j in range(6):
        if(j==0 )or (i==6)and(j>0):
            print("*",end="")
        else:
            print(end=" ")
    print()
print()

#pattern M
for i in range(7):
    for j in range(6):
        if(j==0 or j==5) or((i==j)and(j>0 and j<3)) or(i==1 and j==4)or(i==2 and j==3):
            print("*",end="")
        else:
            print(end=" ")
    print()
print()
#pattern N
for i in range(7):
    for j in range(6):
        if(j==0 or j==5) or((i==j)and(j>0)):
            print("*",end="")
        else:
            print(end=" ")
    print()
print()

#pattern O:
for i in range(7):
    for j in range(6):
        if((j==0 and i!=0 and i!=6 )or (j==4 and i!=0 and i!=6)) or ((i==0 or i==6) and (j>0 and j<4)):
            print("*",end="")
        else:
            print(end=" ")
    print()
print()

#pattern p
for i in range(7):
    for j in range(6):
        if(j==0) or ((i==0 or i==3 )and (j>0 and j<4)) or ((i==1 or i==2) and (j>3)and j<=4):
            print("*",end="")
        else:
            print(end=" ")
    print()
print()
#pattern Q
for i in range(7):
    for j in range(6):
        if((j==0 and i!=0 and i!=6 )or (j==3 and i!=0 and i!=6)) or (i==6 and j==4) or ((i==0 or i==6) and (j>0 and j<3)):
            print("*",end="")
        else:
            print(end=" ")
    print()
print()

#pattern R
for i in range(7):
    for j in range(6):
        if(j==0) or (i==0 or i==3)and (j>0 and j<4) or ((i==1 or i==2) and (j==4)) or (i==j+2 and j>0 and j<=4 ):
            print("*",end="")
        else:
            print(end=" ")
    print()
print()

#pattern S
for i in range(7):
    for j in range(6):
        if(j==0 and i!=0 and i!=4 and i!=3 and i!=5) or( j==4 and i!=1 and i!=3 and i!=6 and i!=2) or(i==0 or i==3 or i==6)and (j>0 and j<4):
            print("*",end="")
        else:
            print(end=" ")
    print()
print()

#pattern T
for i in range(7):
    for j in range(6):
        if(j==2) or (i==0 and j>=0 and j<=4):
            print("*",end="")
        else:
            print(end=" ")
    print()
print()

#pattern u
for i in range(7):
    for j in range(6):
        if(j==0 and i!=6) or (j==4 and i!=6 ) or (i==6 and j>0 and j<4):
            print("*",end="")
        else:
            print(end=" ")
    print()
print()

#pattern V
for i in range(7):
    for j in range(6):
        if(i==j) and (j<3) or (i==0 and j==5)or (i==1 and j==4 )or (i==2 and j==3 ):
            print("*",end="")
      
           
        else:
            print(end=" ")
    print()
print()

#pattern W

for i in range(7):
    for j in range(6):
        if(j==0 or j==5) and (i<5) or ( i==2 and j>=2 and j<=3) or (i+j==4 and i!=1 and i!=0) or (i==3 and j==4):
            print("*",end="")
        
        else:
            print(end=" ")
    print()
print()
#pattern X

for i in range(7):
    for j in range(6):
        if(i==j)or (i+j==5):
            print("*",end="")
        
        else:
            print(end=" ")
    print()
print()

#pattern Y  
for i in range(7):
    for j in range(6):
        if(i==j)and (j>0 and j<4) or (j==3 and i!=0 and i!=1 and i!=2)or (i==2 and j==4) or (i==1 and j==5) :
            print("*",end="")
        else:
            print(end=" ")
    print()
print()

#patter Z

for i in range(7):
    for j in range(6):
        if(i==0 or i==5)or (i+j==5):
            print("*",end="")
       
        else:
            print(end=" ")
    print()
print()

