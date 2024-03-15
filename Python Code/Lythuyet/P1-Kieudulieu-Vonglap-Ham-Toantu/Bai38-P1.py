#BAI 38: LUYEN TAP VIET HAM

from math import*

#1. Kiem tra n la snt dung in 1 sai in 0
def prime(n):
    if n<2: return False
    for i in range(2,int(sqrt(n))+1):
        if n%i==0:
            return False
    return True

#2. In ra tong chu so cua n
def sumNum(n):
    sum=0
    while(n!=0):
        sum+=n%10
        n//=10
    return sum

#3. In ra tong chu so chan cua n
def sumEven(n):
    sum=0
    while(n!=0):
        tmp=n%10
        if tmp%2==0:
            sum+=tmp
        n//=10
    return sum

#4. In tong chu so cua n la so nguyen to
def sumPrime(n):
    sum=0
    while(n!=0):
        tmp=n%10
        if prime(tmp):
            sum+=tmp
        n//=10
    return sum

#5. In so lat nguoc cua n
def numRev(n):
    rev=0
    while(n!=0):
        rev=rev*10+n%10
        n//=10
    return rev

#6. In so luong uoc cua n la so nguyen to
def amuontPrime(n):
    cnt=0
    for i in range(1,int(sqrt(n))+1):
        if n%i==0:
            cnt+=1
            while(n%i==0):
                n//=i
    if n>1: cnt+=1
    return cnt

#7. In uoc nguyen to lon nhat cua n
def maxPrime(n):
    num_max=0
    for i in range(1,int(sqrt(n))+1):
        if n%i==0:
            while(n%i==0):
                num_max=max(num_max,n//i)
                n//=i
    if n>1: num_max=n
    return num_max

#8. Kiem tra neu n ton tai it nhat 1 so 6, dung in 1 sai in 0
def checkNum(n):
    while(n!=0):
        res=n%10
        if(res==6):
            return True
        n//=10
    return False

#9. Kiem tra neu tong chu so cua n chia het cho 8, dung in 1 sai in 0
def checkNum1(n):
    sum=0
    while(n!=0):
        sum+=n%10
        n//=10
    return sum%8==0

#10. Tinh tong giai thua cac chu so cua n roi in ra
def factorialNum(n):
    sum=0
    while(n!=0):
        sum+=factorial(n%10)
        n//=10
    return sum

#11. Kiem tra xem n co duoc tao boi dung 1 so hay khong, dung in 1 sai in 0
def checkNum2(n):
    pre=n%10
    next=0
    while(n!=0):
        next=n%10
        if next!=pre:
            return False
        n//=10
    return True

#12. Kiem tra chu so hang don vi cua n co phai la chu so lon nhat trong n hay khong, dung in 1 sai in 0
def checkNum3(n):
    num_max=n%10
    while(n!=0):
        if(n%10>num_max):
            return False
        n//=10
    return True

#13. In ra tong luy thua cua n voi mu la so chu so
def sumExponent(n):
    cnt=0
    temp=n
    while(temp!=0):
        cnt+=1
        temp//=10
    sum=0
    while(n!=0):
        sum+=(n%10)**cnt
        n//=10
    return sum
    