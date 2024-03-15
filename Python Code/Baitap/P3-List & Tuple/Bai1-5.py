from math import*

#Bai1: Dem chan le va tong chan le
def func(a,n):
    dem_chan,dem_le,tong_chan,tong_le=0,0,0,0
    for i in range(n):
        if a[i]%2==0:
            dem_chan+=1
            tong_chan+=a[i]
        else:
            dem_le+=1
            tong_le+=a[i]
    print(dem_chan)
    print(dem_le)
    print(tong_chan)
    print(tong_le)


#Bai2: Trung binh cong nguyen to
def prime(n):
    if n<2: return False
    for i in range( 2,int(sqrt(n))+1):
        if n%i==0:
            return False
    return True

def gpa(a,n):
    dem=0
    res=0
    for i in a:
        if prime(i):
            dem+=1
            res+=i
    if dem!=0:
        print("{:.2f}".format(res//dem))
    else:
        print("NO")

if __name__=="__main__":
    n=int(input())
    a=list(map(int,input().split()))
    gpa(a,n)  
    