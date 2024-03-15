from math import*

#Bai1: Tong 1
def sum1(n):
    if n==0:
        return 0
    return n + sum1(n-1)

#Bai2: Tong 2
def sum2(n):
    if n==0:
        return 0
    return n**2 + sum2(n-1)

#Bai3: Tong 3
def sum3(n):
    if n==0:
        return 0
    return n**3 + sum3(n-1)

#Bai4: Tong 4
def sum4(n):
    if n==0:
        return 0
    if n%2==0:
        return n + sum4(n-1)
    else:
        return -n + sum4(n-1) 

#Bai5: Tong 5
def sum5(n):
    if n==0:
        return 1
    return n*sum5(n-1)


if __name__=="__main__":
    n=int(input())
    print(sum5(n))