#BAI 68: KY THUAT CUA SO TRUOT
if __name__=="__main__":
    n=int(input())
    a=list(map(int,input().split()))
    k=int(input())
    
    tong1=0
    for i in range(k):
        tong1+=a[i]
    print(tong1,end=" ")

    for i in range(k,n):
        tong1=tong1-a[i-k]+a[i]
        print(tong1,end=" ")
    