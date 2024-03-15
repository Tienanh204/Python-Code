
#Bai6: So Fibonacci
def fibo(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)
    

#Bai7: Tinh to hop hap K cua N
def nCk(n,k):
    if k==0 or k==n:
        return 1
    return nCk(n-1,k-1)+nCk(n-1,k)

#Bai8: UCLN & BCNN
def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)

def lcm(a,b):
    return a*b//gcd(a,b)

#Bai9: Luy thua nhi phan (a^b) -> HAY
"""
- Neu tinh bth rat lau ta co cach tinh sau:
      { 1, neu b=0
a^b = { a^(b/2) * a^(b/2), neu b chan
      { a^(b/2) * a^(b/2)) * a, neu b le
"""

def binpow(a,b):
    if b==0:
        return 1
    x = binpow(a,b//2)    #luc truy nguoc lai de tinh binpow(2,10) -> no se bat dau tu dong nay do xuong

    if b%2==0:
        return x*x % (10**9+7)
    else:
        return x*x*a % (10**9+7)


#Bai10: Tong 5
def sum5(n):
    if n==1:
        return 1
    return 1/n + sum5(n-1)

if __name__=="__main__":
     n=int(input())
     print("{:.3f}".format(sum5(n)))
