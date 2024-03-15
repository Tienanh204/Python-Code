from math import*

#Bai21: Binh phuong nguyen to 1
"""
- Ban chat la phan tich thua so nguyen to ma trong do ton tai
mot thua so nguyen to co so mu toi thieu bang 2 
"""

def numBeauty(n):
    for i in range(2,int(sqrt(n))+1):
        if n%i==0:
            mu=0
            while(n%i==0):
                mu+=1
                n//=i
            if mu>=2: return True
    return False


#Bai22: Binh phuong nguyen to 2 (De -> Bo qua)
 
#Bai23: Goldbach conjecture

def prime(n):
    if n<2: return False
    for i in range(2,int(sqrt(n))+1):
        if n%i==0:
            return False
    return True


def goldbach(n):
    for i in range(2,n//2 +1):
        if prime(i) and prime(n-i):
            print(i,n-i,sep=" ")

#Bai24: So nguyen duong nho nhat chia het cho x,y,z
"""
- Duyet nhu binh thuoc se bi time limited nen la ta dung cach sau:
tim bcnn cua x,y,z dua ve bai toan --> tim so nho nhat >= 10**(n-1) chia het cho bcnn
*cong thuc: so nho nhat hia het cho n nam trong doan [a,b]
((a+n-1)//n)*n ---> Nho ai nay nhaaaaaaaaaaaaaaaaaaaaaaa
"""
def gcd(a,b):
    while(b!=0):
        a,b=b,a%b
    return a
def lcm(a,b):
    return a*b//gcd(a,b)

def minNum(x,y,z,n):
    bcnn=lcm(lcm(x,y),z)
    tmp=10**(n-1)
    ans=(tmp+bcnn-1)//bcnn * bcnn

    if ans<10**n:
        return ans
    return -1

#Bai25: Cap so nguyen to cung nhau

def primeCouple(a,b):
    for i in range(a,b):
        for j in range(i+1,b+1):
            if gcd(i,j)==1:
                print("(",i,",",j,")", sep="")


if __name__=="__main__":
    a,b=map(int,input().split())
    primeCouple(a,b)






    

        

