from math import*
#Bai21: Kiem tra mang doi xung
def checkA(a,l,r):
    if l >= r:
        return True
    else:
        if a[l] != a[r]:
            return False
        else:
            return checkA(a,l+1,r-1)
        
#Bai22: In mang
def in1(a,n):
    if n>=1:
        print(a[n-1],end=" ")
        in1(a,n-1)

def in2(a,n):
    if n>=1:
        in2(a,n-1)
        print(a[n-1],end=" ")

#Bai23: Kiem tra mang toan chan
def check(a,n):
    if n>=1:
        if a[n-1]%2!=0:
            return False
        else: check(a,n-1)
    else:
        return True

#Bai24: Kiem tra mang tang dan
def ascending(a,n):
    if n==1:
        return True
    else:
        if a[n-1]<=a[n-2]:
            return False
        else:
            return ascending(a,n-1)
        
#Bai25: Binary search

def binarySearch(a,x,l,r):
    if l>r:
        return False
    
    m=(r+l)//2
    if a[m]==x:
        return True
    
    if a[m] < x:
        return binarySearch(a,x,m+1,r)
    
    if a[m]>x:
        return binarySearch(a,x,l,m-1)

if __name__=="__main__":
    n=int(input())
    a=list(map(int,input().split()))
    x=int(input())
    if binarySearch(a,x,0,n-1):
        print("YES")
    else:
        print("NO")