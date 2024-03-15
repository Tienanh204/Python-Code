from math import*

#Bai16: Liet ke

#Bai17: Mang doi xung
def doixung(a,n):
    for i in range(n//2):
        if a[i]!=a[n-i-1]:
            return False
    return True

#Bai18: Lien ke trai dau
def func(a,n):
    for i in range(n):
        if i==0:
            if a[i]*a[i+1]<0:
                print(a[i],end=" ")
        elif i==n-1:
            if a[i]*a[i-1]<0:
                print(a[i],end="")
        else:
            if a[i]*a[i+1]<0 or a[i]*a[i-1]<0:
                print(a[i],end=" ")



if __name__=="__main__":
    n=int(input())
    a=list(map(int,input().split()))
    func(a,n)

