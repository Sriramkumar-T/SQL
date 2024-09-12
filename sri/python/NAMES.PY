def pattern():
    for a in range(len(name)):
        if name[a]=="a":
            print_A=[[" "for col in range(6)]for row in range(7)]
            for i in range(7):
                for j in range(6):
                         if((j==0 or j==4 ) and (i!=0)) or ((i==0 or i==3)and (j>0 and j<4)):
                                print_A[i][j]="*"
            list2.append(print_A) 

        elif name[a]=="b":
            print_B=[[" "for col in range(6)]for row in range(7)]  
            for i in range(7):
                for j in range(6): 
                    if((j==0 )or (j==4 and i!=0 and i!=3 and i!=6)) or ((i==0 or i==3 or i==6) and (j>0 and j<4)):
                        print_B[i][j]="*"
            list2.append(print_B)

        elif name[a]=="c":
            print_C=[[" "for col in range(5)]for row in range(7)]
            for i in range(7):
                for j in range(6):
                    if(j==0 and (i!=0 and i!=6) )or((i==0 or i==6)and(j>0)):
                        print_C[i][j]="*"
            list2.append(print_C)
        
        elif name[a]=="d":
            print_D=[[" "for col in range(6)]for row in range(6)]
            for i in range(7):
                for j in range(6):
                    if(j==0 or (j==5 and (i!=0 and i!=6))) or ((i==0 or i==6)and(j>0 and j<5)) :
                        print_D[i][j]="*"
            list2.append(print_D)
        

        elif name[a]=="e":
            print_E=[[" "for col in range(6)]for row in range(7)]
            for i in range(7):
                for j in range(6):
                    if(j==0  ) or ((i==0 or i==3 or i==6)and(j>0)): 
                        print_E[i][j]="*"
            list2.append(print_E)
        

        elif name[a]=="f":
            print_F=[[" "for col in range(6)]for row in range(7)]
            for i in range(7):
                for j in range(6):
                    if(j==0 and i!=2) or ((i==0 or i==2)and(j>0)):
                        print_F
            list2.append(print_F)
        

        elif name[a]=="g":
            print_G=[[" "for col in range(6)]for row in range(7)]
            for i in range(7):
                for j in range(6):
                    if((j==0 and i!=0) or (j==4 and i!=2 and i!=3 )) or ((i==0 or i==6)and (j>0 and j<4)) or (j==3 and i==4):
                        print_G[i][j]="*"
            list2.append(print_G)
        

        elif name[a]=="h":
            print_H=[[" "for col in range(6)]for row in range(7)]
            for i in range(7):
                for j in range(6):
                    if(j==0 or j==4)or((i==3) and (j>0 and j<4)):
                        print_H[i][j]="*"
            list2.append(print_H)
        

        elif name[a]=="i":
            print_I=[[" "for col in range(6)]for row in range(7)]
            for i in range(7):
                for j in range(6):
                    if(j==2)or((i==0 or i==6) and (j<=4)):
                        print_I[i][j]="*"
            list2.append(print_I)
        
        elif name[a]=="j":
            print_J=[[" "for col in range(6)]for row in range(7)]
            for i in range(7):
                for j in range(6):
                    if((j==0)and( i!=1 and i!=2 and i!=3 and i!=4 and i!=6) or (j==3)) or (( i==0 or i==6)and(j<4)):
                        print_J[i][j]="*"
            list2.append(print_J)
        

        elif name[a]=="k":
            print_K=[[" "for col in range(6)]for row in range(7)]
            for i in range(7):
                for j in range(6):
                    if(j==0)or (i+j==3 or i-j==2):
                        print_K[i][j]="*"
            list2.append(print_K)
        

        elif name[a]=="l":
            print_L=[[" "for col in range(6)]for row in range(7)]
            for i in range(7):
                for j in range(6):
                    if(j==0 )or (i==6)and(j>0):
                        print_L[i][j]="*"
                list2.append(print_L)
        
        elif name[a]=="m":
            print_M=[[" "for col in range(6)]for row in range(7)]
            for i in range(7):
                for j in range(6):
                    if(j==0 or j==5) or((i==j)and(j>0 and j<3)) or(i==1 and j==4)or(i==2 and j==3):
                        print_M[i][j]="*"
            list2.append(print_M)
        
        
        elif name[a]=="n":
            print_N=[[" "for col in range(6)]for row in range(7)]
            for i in range(7):
                for j in range(6):
                   if(j==0 or j==5) or((i==j)and(j>0)):
                        print_N[i][j]="*"
            list2.append(print_N)
        

        elif name[a]=="o":
            print_O=[[" "for col in range(6)]for row in range(7)]
            for i in range(7):
                for j in range(6):
                    if((j==0 and i!=0 and i!=6 )or (j==4 and i!=0 and i!=6)) or ((i==0 or i==6) and (j>0 and j<4)):
                        print_O[i][j]="*"
            list2.append(print_O)
        

        elif name[a]=="p":
            print_P=[[" "for col in range(6)]for row in range(7)]
            for i in range(7):
                for j in range(6):
                    if(j==0) or ((i==0 or i==3 )and (j>0 and j<4)) or ((i==1 or i==2) and (j>3)):
                        print_P[oi][j]="*"
            list2.append(print_P)
        

        elif name[a]=="q":
            print_Q=[[" "for col in range(6)]for row in range(7)]
            for i in range(7):
                for j in range(6):
                    if((j==0 and i!=0 and i!=6 )or (j==3 and i!=0 and i!=6)) or (i==6 and j==4) or ((i==0 or i==6) and (j>0 and j<3)):
                        print_Q[i][j]="*"
            list2.append(print_Q)


        elif name[a]=="r":
            print_R=[[" "for col in range(6)]for row in range(7)]
            for i in range(7):
                for j in range(6):
                    if(j==0) or (i==0 or i==3)and (j>0 and j<4) or ((i==1 or i==2) and (j>3)and (j<=4) )or (i==j+2 and j>0 and j<5 ):
                        print_R[i][j]="*"
            list2.append(print_R)
        

        elif name[a]=="s":
            print_S=[[" "for col in range(6)]for row in range(7)]
            for i in range(7):
                for j in range(6):
                    if(j==0 and i!=0 and i!=4 and i!=3 and i!=5) or( j==4 and i!=1 and i!=3 and i!=6 and i!=2) or(i==0 or i==3 or i==6)and (j>0 and j<4):
                        print_S[i][j]="*"
            list2.append(print_S)
        

        elif name[a]=="t":
            print_T=[[" "for col in range(6)]for row in range(7)]
            for i in range(7):
                for j in range(6):
                    if(j==2) or (i==0 and j>=0 and j<=4):
                        print_T[i][j]="*"
            list2.append(print_T)
        

        elif name[a]=="u":
            print_U=[[" "for col in range(6)]for row in range(7)]
            for i in range(7):
                for j in range(5):
                    if(j==0 and i!=6) or (j==4 and i!=6 ) or (i==6 and j>0 and j<4):
                        print_U[i][j]="*"
            list2.append(print_U)
        

        elif name[a]=="v":
            print_V=[[" "for col in range(6)]for row in range(7)]
            for i in range(7):
                for j in range(6):
                    if(i==j) and (j<3) or (i==0 and j==5)or (i==1 and j==4 )or (i==2 and j==3 ):
                        print_V[i][j]="*"
            list2.append(print_V)
        

        elif name[a]=="w":
            print_W=[[" "for col in range(6)]for row in range(7)]
            for i in range(7):
                for j in range(6):
                    if(j==0 or j==5) and (i<5) or ( i==2 and j>=2 and j<=3) or (i+j==4 and i!=1 and i!=0) or (i==3 and j==4):
                        print_W[i][j]="*"
            list2.append(print_W)

        
        elif name[a]=="x":
            print_X=[[" "for col in range(6)]for row in range(7)]
            for i in range(7):
                for j in range(6):
                    if(i==j)or (i+j==5):
                        print_X[i][j]="*"
            list2.append(print_X)
        
        elif name[a]=="y":
            print_Y=[[" "for col in range(6)]for row in range(7)]
            for i in range(7):
                for j in range(6):
                    if(i==j)and (j>0 and j<4) or (j==3 and i!=0 and i!=1 and i!=2)or (i==2 and j==4) or (i==1 and j==5) :
                        print_Y[i][j]="*"
            list2.append(print_Y)
        

        elif name[a]=="z":
            print_Z=[[" "for col in range(6)]for row in range(7)]
            for i in range(7):
                for j in range(6):
                    if(i==0 or i==5)or (i+j==5):
                        print_Z[i][j]="*"
            list2.append(print_Z)
        
        else:
            print("invalid")
    return list2

name=input("enter a name: ")
list2=[]
list3=pattern()

for row in range(7):
    for col in range(len(list3)):
        for k in range(6):
            print(list3[col][row][k],end=" ")
        print(end="  ")
    print()
print()

        

