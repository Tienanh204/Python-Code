n,m=map(int,input().split())

min_step=0
max_step=n

if n%2==0:
    min_step=n//2
else:
    min_step=n//2+1

ans=(min_step+m-1)//m*m

if(ans<=max_step):
   print(ans)
else:
   print(-1)