#BAI 36: SO HOAN HAO VA DINH LY EUCLID - EULER

import math

#1. So hoan hao
"""
Một số tự nhiên g được gọi là "số hoàn hảo" nếu tổng các ước số dương của g (trừ chính nó) bằng chính nó.
Nói cách khác, số hoàn hảo là số mà tổng các ước số của nó (không tính chính nó) chính bằng nó.

VD: n=28, uoc la 1+2+4+7+14=28
"""
#ycbt 0<=n<=9*10^10

def perfectNum1(n):
    res=1 
    for i in range(2,math.isqrt(n)+1):
        if n%i==0:
          res+=i
          if i!=n//i :
                res+=n//i
    return res==n



#2. Dinh ly EUCLID - EULER

"""
- Ta thay cac kiem tra so hoan hao ben tren cung rat tot roi.
Nhung neu n ma qua lon thi no van chay rat la lau, do do
ta phai co cach khac do chinh la su dung --> Dinh ly EUCLID - EULER

*Dinh ly:
. Neu p la so nguyen to va 2^p - 1 cung la so nguyen to ==> (2^p - 1) * 2^(p-1) la 1 so hoan hao

"""

# ycbt 0<=N<=9*10^18

def prime(n):
    if n<2 : return False
    for i in range(2,math.isqrt(n)+1):
        if n % i==0:
            return False
    return True

def perfectNum2(n):
    for p in range(2,33): #duyet tam 35 so hoan hao dau tien (thuong thi so hoan hao rat it nen duyet tung do la du roi)
        if prime(p) and prime(2**p-1):
            hh=(2**p-1) * 2**(p-1)
        if hh==n: #Ta co the commentline dieu kien nay va print(hh) va xem duoc [0,9*10^18] chi co 8 so hoan hao --> rat it
            return True
    return False


if __name__=="__main__":
    n=int(input())
    print(perfectNum1(n))
    print(perfectNum2(n))