n=int(input())

ans=0
res=0

if(n>=100):
    res+=n//100
    n=n%100
if(n>=20):
    res+=n//20
    n=n%20
if(n>=10):
    res+=n//10
    n=n%10
if(n>=5):
    res+=n//5
    n=n%5
if(n>=1):
    res+=n
print(res)