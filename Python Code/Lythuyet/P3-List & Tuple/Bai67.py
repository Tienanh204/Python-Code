#BAI 67: MANG CONG DON (PREFIX SUM)

"""
- Bài toán đặt ra: Cho mảng A[] có N phần tử, yêu cầu truy vấn
tổng các phần tử từ chỉ số l -> chỉ số r

"""
def prefixSum(a,f,n):
    for i in range(n):
        if i==0:
            f[0]=a[i]
        else:
            f[i]=f[i-1]+a[i]
    


if __name__=="__main__":
    n=int(input())
    f=[0]*(n+1)
    a=list(map(int,input().split()))
    l=int(input())
    r=int(input())
    prefixSum(a,f,n)
    print(f[r]-f[l-1])
    