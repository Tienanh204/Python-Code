n=int(input())

if n%2==0:
    print("YES")
else:
    print("NO")

if n%3==0 and n%5==0:
    print("YES")
else:
    print("NO")

if n%3==0 and n%7!=0:
        print("YES")
else:
    print("NO")

if n%3==0 or n%7==0:
    print("YES")
else:
    print("NO")

if n>30 and n<50:
    print("YES")
else:
    print("NO")

if n>=30 and (n%2==0 or n%3==0 or n%5==0):
    print("YES")
else:
    print("NO")


r=n%10
if (n>=10 and n < 100) and (n==3 or n==5 or n==2 or n==7):
    print("YES")
else:
    print("NO")

if n<=100 and n%23==0:
    print("YES")
else:
    print("NO")

if (n<10 or n>20) and (r%3==0):
    print("YES")
else:
    print("NO")