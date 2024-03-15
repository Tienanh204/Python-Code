#BAI 30: PHAN TICH THUA SO NGUYEN TO

from math import*

def ptich(n):
    for i in range(2,int(sqrt(n))+1):
        if n%i==0:
         while(n%i==0):
            print(i,end=" ")
            n//=i;
    if n>1:#TH n la so nguyen to (boi vi no la so nguyen to nen no khong the chia het cho bat cu so nao [2,sqrt(n)+1] --> nen phan tich ra la chinh no 
        print(n)

if __name__=="__main__":
    n=int(input())
    ptich(n)

#NOTE: Tu phan tich thua so nguyen to ta co the --> so uoc cua so do

"""
- Trong toan roi rac da hoc
n=p1^l1 x p2^l2 x p3^l3 ..... x pk^lk
---> so uoc cua n: d(n)=(l1+1)x(l2+1)x(l3+1)....(lk+1)
"""