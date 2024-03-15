from math import*

#Bai16: So gan thuan nghich

def palindrome(n):
    temp_n=n
    rev=0
    while(n!=0):
        rev=rev*10 + n%10
        n//=10
    return rev==temp_n


def nearPalindrome(n):
    last=n%10
    rev=0
    n=n//10
    while(n!=0):
        rev1=rev1*10 + n%10
        n//=10
    first=rev%10

    if first == 2*last or last == 2*first:
       if palindrome(rev//10):
        return True
    return False

#Bai17: UCLN & BCNN
def gcd(a,b):
   while(b!=0):
        a,b=b,a%b
   return a   
def lcm(a,b):
   return (a*b)//gcd(a,b)


#Bai18: Bieu dien so
#Bai19: So hoan hao
def Prime(n):
    if n<2: return False
    for i in range(2,int(sqrt(n))+1):
        if n%i==0:
            return False
    return True

def numPerfect(n):
   for p in range(2,33):
        if Prime(p) and Prime(2**p - 1):
            if n == (2**p - 1) * 2**(p-1):
                return True
   return False

#Bai20: Thua so nguyen to thu K

def digitalPrime(n,k):
    cnt=0
    res=0
    for i in range(2,int(sqrt(n))+1):
        if n%i==0:
            while(n%i==0):
                cnt+=1
                if cnt==k:
                    return  i
                n//=i
    if n!=1:
        cnt+=1
        if cnt==k:
            return n
    return -1


if __name__=="__main__":
   n,k=map(int,input().split())
   print(digitalPrime(n,k))







    
    




    