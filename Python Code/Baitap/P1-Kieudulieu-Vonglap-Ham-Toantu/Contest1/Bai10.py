from math import*

a,b,c=map(int,input().split())

if a<0 or b<0 or c<0:
    print("NO")
elif (a+b<=c) or (a+c<=b) or (b+c<=a):
    print("NO")
else:
    print("YES")