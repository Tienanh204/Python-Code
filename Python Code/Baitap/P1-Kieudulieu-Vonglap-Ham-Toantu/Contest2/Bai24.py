from math import*

a,b=map(int,input().split())

ga,gb=1,1

for i in range(1,a+1):
    ga*=i

for i in range(1,b+1):
    gb*=i

while(ga*gb!=0):
    if a>b:
        ga%=gb
    else:
        gb%=ga

print(ga+gb)
