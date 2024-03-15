from math import*

x,y=map(int,input().split())

print(x+y)
print(x-y)
print(x*y)

if y==0:
    print("INVALID")
else:
    print("{:.4f}".format(x/y))