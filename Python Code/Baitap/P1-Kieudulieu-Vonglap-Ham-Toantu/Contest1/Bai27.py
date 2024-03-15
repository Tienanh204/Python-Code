from math import*
a=float(input())

if(a-floor(a)>=0.5):
    print(ceil(a))
else:
    print(floor(a))