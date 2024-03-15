from math import*
n=int(input())

res=0

for i in range(1,int(sqrt(n))):
    if(n%i==0):
        if(i==n//i):
         res=res+i
        else:
         res=res+i+n//i #tranh TH n la so chinh phuong
print(res)
