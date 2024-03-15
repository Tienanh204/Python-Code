from math import*

n=int(input())

for i in range(1,n+1):
    if sqrt(i)==int(sqrt(i)):
        print(i,end=" ")