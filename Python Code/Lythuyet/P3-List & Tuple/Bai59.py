#BAI 59: 3 DANG TOAN CO BAN TREN MANG 1 CHIEU (LIST)
from math import*
#Baitoan1: Liet ke, dem cac phan tu thoa man tinh chat nao do tỏng list

#Baitoan2: Tim max, min
n=int(input())
a=list(map(int,input().split()))
res=0
for i in range(len(a)):
    res=max(res,a[i])
print(res)
    
res=a[0]
for i in range(len(a)):
    if res<a[i]:
        res=a[i]
print(res)

#Baitoan3: Kiem tra cac cap phan tu trong list thoa man dieu kien gì do
for i in range(n-1):
    for j in range(i+1,n):
        print(a[i],a[j])
