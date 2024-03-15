#BAI 28: TINH TONG UOC VA DEM OC CUA MOT SO NGUYEN


"""
Code Trau va code toi uu de thay ro, 
nen dung code toi uu nghe chua la code
chay tu 1->sqrt(n) okokokok
"""

#1. Tinh tong uoc

from math import*
def tong1(n):#code trau
    res=0
    for i in range(1,n+1):
        if(n%i==0):
              res+=i
    return res

def tong2(n):#code toi uu
     res=0
     for i in range(1,int(sqrt(n))+1):
          if n%i==0:
            res+=i
            if i!=n//i:
                res+=n//i
     return res

#2. Dem uoc

def dem1(n):#code trau
    res=0
    for i in range(1,n+1):
        if(n%i==0):
              res+=1
    return res

def dem2(n):#code toi uu
     res=0
     for i in range(1,int(sqrt(n)+1)):
          if n%i==0:
            res+=1
            if i!=n//i:
                res+=1
     return res


if __name__=="__main__":
     n=int(input())
     print(tong1(n))
     print(tong2(n))
     print(dem1(n))
     print(dem2(n))