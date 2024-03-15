#BAI 70: CONTEST 6 (SANG SO NGUYEN TO, MANG CONG DON)
from math import*

#Bai1: Giai thua chia du
f=[0]*(10**6+1)

def giaithua():#Khoi tao 10**6 gia thua dau tien
    f[0]=1
    for i in range(1,10**6+1):
       f[i]=f[i-1]*i
       f[i]%=(10**9+7)


#Bai2: Fibonacci
fibo=[0]*(1000001+1)
def fibonacci():
    fibo[0],fibo[1]=0,1
    for i in range(2,10**6+1):
        fibo[i]=fibo[i-1]+fibo[i-2]
        fibo[i]%=(10**9+7)

#Bai3: Tribonacci (De->Bo qua)

#Bai4: Prime 1
prime=[True]*(10**6+1)
primeArr=[0]*(10**6+1)
def init():
    #Sang so nguyen to bang Eratosthenet
    prime[0],prime[1]=False,False
    for i in range(2,int(sqrt(10**6))+1):
        if prime[i]:
            for j in range(i*i,10**6+1,i):
                prime[j]=False
    primeArr[0]=primeArr[1]=0
    cnt=0
    for i in range(2,int(sqrt(10**6))+1):
        if prime[i]:
            cnt+=1
        primeArr[i]=cnt


if __name__=="__main__":
    init()
    t=int(*input())
    for i in range(t):
        n=int(input())
        print(primeArr[n])


        




