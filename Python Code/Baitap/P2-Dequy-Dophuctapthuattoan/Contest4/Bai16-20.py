from math import*

#Bai16: Chu so lon nhat va nho nhat
def minN(n):
    if n<10:
        return n
    return min(n%10,minN(n//10))

def maxN(n):
    if n<10:
        return n
    return max(n%10,maxN(n//10))

#Bai17: In ra so nguyen
def integer1(n):
    if n!=0:
        integer1(n//10)
        print(n%10,end=" ")

def integer2(n):
     if n!=0:
        print(n%10,end=" ")
        integer2(n//10)


#Bai18: Tinh tong hu so chan le
def chan(n):
    if n<10:
        if n%2==0:
            return n
        else:
            return 0
    else:
        if n%2==0:
            return n%10 + chan(n//10)
        else:
            return chan(n//10)

def le(n):
    if n<10:
        if n%2!=0:
            return n
        else:
            return 0
    else:
        if n%2!=0:
            return n%10 + le(n//10)
        else:
            return le(n//10)

#Bai19: Kiem tra chu so chan
def checkNum(n):
    if n<10:
        if n%2==0:
            return True
        else:
            return False
    else:
        if n%2!=0:
            return False
        else:
            return checkNum(n//10)

#Bai20: Dem so thao tac
def cnt(n):
    if n==1:
        return 0
    tt1,tt2,tt3=10**9.10**9,10**9
    if n%2==0:
        tt1=1+cnt(n//2)
    if n%3==0:
        tt2=1+cnt(n//3)
    if n>1:
        tt3=1+cnt(n-1)
    return min(tt1,tt2,tt3)    


if __name__=="__main__":
    n=int(input())
