from math import*


#Bai1: Kiem tra so nguyen to (Da lam)


#Bai2: So Sphenic
def sphenic(n):
    cnt=0
    i=2
    while i<=int(sqrt(n)):# o day thay vi dung vong for thi minh nen dung while
        if(n%i==0):      #vi ta thay n trong code no luon giam n//=10, doi voi for thi sqrt(n) no se du in gia tri ban dau du n o thay doi, con while thi no se cap nhap lai sqrt(n) theo n
            mu=0
            while(n%i==0):
                mu+=1
                n//=10
            if mu>=2: return False
            cnt+=1
    if n>1:
        cnt+=1
    return cnt==3

    
#Bai3: Phan tich thua so nguyen to
def digitalPrime(n):
    for i in range(2,int(sqrt(n))+1):
        if n%i==0:
            mu=0
            while(n%i==0):
                mu+=1
                n//=i
            print(i,mu,sep="^",end="")
            if n!=1:
                print(" * ",end="")
    if n>2: print(n,1,sep="^")

    
#Bai4: Uoc so nguyen to lon nhat (Da lam)


#Bai5: So Smith
def checkPrime(n):
    if n<2: return False
    for i in range(2,int(sqrt(n))+1):
        if n%i==0:
            return True
    return False

def tong(n):
    res=0
    while(n!=0):
        res+=n%10
        n//=10
    return res

def smith(n):
    if checkPrime(n):
        sum_n=tong(n)
        sum_prime=0

        for i in range(2,int(sqrt(n))+1):
            if n%i==0:
                while(n%i==0):
                    sum_prime+=tong(i)
                    n//=i   
        if n>1: sum_prime+=tong(n)

        return sum_n==sum_prime
    
    return False



if __name__=="__main__":

    n=int(input())

