from math import*

"""
//Bai11
a,b,c=map(int,input().split())
if (a>0 and b>0 and c>0) and (a+b>c or a+c>b or b+c>a):
    if a==b and b==c:
        print(1)
    elif a==b or b==c or c==a:
        print(2)
    elif a**2+b**2==c**2 or a**2+c**2==b**2 or b**2+c**2==a**2:
        print(3)
    else:
        print(4)
else:
    print("INVALID")

    
//Bai12
t,n=map(int,input().split())

if (t<=12 and t>=1) and (n>0):
    if(n%400==0):
        if(t==2): print(29)
        elif(t==4 or t==6 or t==9 or t==11): print(30)
        else: print(31)
    else:
        if(t==2): print(28)
        elif(t==4 or t==6 or t==9 or t==11): print(30)
        else: print(31)
else:
    print("INVALID")

    
//Bai15
n,a,b=map(int,input().split())

if(a<=(b/2)):
    print(a*n)
else:
    print(((n//2)*b)+n%2*a)
"""
