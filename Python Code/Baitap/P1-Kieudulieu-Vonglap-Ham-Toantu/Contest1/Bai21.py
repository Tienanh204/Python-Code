a,b,k=map(int,input().split())

if(k%2==0):
    print (k//2*a-k//2*b)
else:
    print((k+1)//2*a-k//2*b)