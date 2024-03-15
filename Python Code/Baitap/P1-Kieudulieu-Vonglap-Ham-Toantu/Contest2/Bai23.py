from math import*

n=int(input())

res=1
for i in range(1,n+1):
    for j in range(1,n+1):
        print(res,end=" ")
        res+=1
    print()
print()

for i in range(1,n+1):
    for j in range(0,n):
        print(i+j,end=" ")
    print()
print()

for i in range(1,n+1):
    for j in range(n,0,-1):
        if(j<=i):
            print(i,end="")
        else:
            print("~",end="")
    print()
print()

for i in range(1,n):
    ktao=i
    kcach=n-1
    for j in range(0,i):
        print(ktao,end=" ")
        ktao+=kcach
        kcach-=1
    print()
print()

