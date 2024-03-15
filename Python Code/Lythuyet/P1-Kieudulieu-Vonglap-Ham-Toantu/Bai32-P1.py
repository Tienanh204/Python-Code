#BAI 32: UOC CHUNG LON NHAT VA BOI CHUNG NHO NHAT

from math import*

#1. UCLN
"""
- Thuat toan tim ucln bang Euclid

         { a (b==0)
gcd(a,b)={
         { gcd(b,a%b)
         
"""

def gcd(a,b):
    while(b!=0):
        a,b=b,a%b
    return a+b


#2. BCNN

def lcm(a,b):
    return a*b//gcd(a,b)

#3. Tim UCLN BCNN cua nhieu so (bang cach goi nhieu lan ham gcd)

if __name__=="__main__":
    a,b,c=map(int,input().split())
    print(gcd(gcd(a,b),c))
    print(lcm(lcm(a,b),c))
    