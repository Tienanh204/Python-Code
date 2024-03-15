from math import*

#Bai 11: So thuan nguyen to
def checkPrime(n):
    if n<2: return False
    for i in range(2,int(sqrt(n))+1):
        if n%i==0:
            return False
    return True

def checkPrime1(n):
    while(n!=0):
       if checkPrime(n%10)==False:
            return False
       n//=10
    return True

def checkPrime2(n):
    cnt=0
    while(n!=0):
        cnt+=n%10
        n//=10
    if checkPrime(cnt):
        return True
    return False


def prime(a,b):
    cnt=0
    for i in range(a,b+1):
        if(checkPrime(i) and checkPrime1(i) and checkPrime2(i)):
            cnt+=1
    return cnt


#Bai12: So thuan nghich co 3 uoc nguyen to (Meo: khi ycbt de cap den Uoc nguyen to --> Su dung phan tich thua so nguyen to)
def checkPrime3(n):
    cnt=0
    for i in range(2,int(sqrt(n))+1):
        if n%i==0:
            cnt+=1
            while(n%i==0):
                n//=i
    if n!=1: cnt+=1
    return cnt>=3

def palindrome(n):
    temp_n=n
    rev=0
    while(temp_n!=0):
        rev=rev*10 + temp_n%10
        temp_n//=10
    return rev==n

#Bai13: So loc phat (De om -> khoi lam)


#Bai14: So thuan nghich, loc phat
def checkNum1(n):
    while(n!=0):
        if n%10==6:
            return True
        n//=10
    return False

def checkNum2(n):
    sum=0
    while(n!=0):
        sum+=n%10
        n//=10
    return sum%10==8


#Bai15: Chu so cuoi cung lon nhat
def maxNum(n):
    res=n%10
    while(n!=0):
        if n%10 > res:
            return False
        n//=10
    return True

if __name__=="__main__":
    n=int(input())
    for i in range(2,n+1):
        if maxNum(i) and checkPrime(i):
            print(i,end=" ")
            

    
    



