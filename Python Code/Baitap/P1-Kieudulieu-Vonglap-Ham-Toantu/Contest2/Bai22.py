from math import*

n=int(input())

for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end="")
    print()
print()

for i in range(n,0,-1):
    for j in range(1,i+1):
        print("*",end="")
    print()
print()

for i in range(1,n+1):
    for j in range(n,0,-1):
        if(j<=i):
            print("*",end="")
        else:
            print(" ",end="")
    print()
print()

for i in range(n,0,-1):
    for j in range(n,0,-1):
        if(j<=i):
            print("*",end="")
        else:
            print(" ",end="")
    print()
print()

for i in range(1,n+1):
    for j in range(1,i+1):
        if(j==1 or j==i or i==n):
            print("*",end="")
        else:
            print(" ",end="")
    print()
print()
