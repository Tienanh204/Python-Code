from math import*
from sys import stdin

def lietke(a,n):
    cnt1=[0]*10000001
    for i in range(n):
        cnt1[a[i]]+=1

    cnt2=cnt1.copy()

    for i in range(n):
        if cnt1[a[i]]>=1:
            print(a[i],cnt1[a[i]],sep=" ")
            cnt1[a[i]]=0
    print()

    for i in range(min(a),max(a)+1):
        if cnt2[i]!=0:
            print(i,cnt2[i],sep=" ")
    
    print()

    max_cnt=max(cnt2)
    min_cnt=1
    
    res1,res2=-1e9,1e9

    for i in range(n):
        if cnt2[a[i]]==max_cnt:
            res1=max(res1,a[i])
        if cnt2[a[i]]==min_cnt:
            res2=min(res2,a[i])
    print(res1)
    print()
    print(res2)

#Bai25: Mang han le

if __name__=="__main__":
    a=[]
    for s in stdin:
        a+=list(map(int,s.split()))
    chan,le=0,0
    for x in a:
        if x%2==0:
            chan+=1
        else:
            le+=1
    if chan==le:
        print("CHANLE")
    elif chan>le:
        print("CHAN")
    else:
        print("LE")

