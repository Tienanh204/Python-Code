#BAI 31: SO CHINH PHUONG

from math import*

#1. Can bac 2
"""
ap dung tinh chat n=int(sqrt(n)) * int(sqrt(n))
"""

def square(n):
    if(n==isqrt(n)*isqrt(n)):
        return True
    return False

if __name__=="__main__":
    n=int(input())
    if(square(n)):
        print("YES")
    else:
        print("NO")
