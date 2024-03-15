n=int(input())

cnt=0
for i in range(0,n+1,3):
    if i%3==0:
        cnt+=i

print(cnt)

sum=0
for i in range(1,n+1):
    sum+=1/i

print("{:.3f}".format(sum))