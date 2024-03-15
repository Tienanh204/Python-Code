#BAI 60: KY THUAT MANG DANH DAU

"""
Kỹ thuật mảng đánh giấu rất mạnh giúp giải quyết các bài toán:
1. Gía trị khác nhau trong mảng: Tìm số lượng phần tư rkhacs nhau, liệt kê
2. Những bài toán tần suất xuất hiện

Mấu chốt: Dùng chỉ số của mảng để đánh giấu giá trị tương ứng
và chỉ áp dụng với những số 0<= x <=10^7
"""
if __name__=="__main__":
    n=int(input())
    a=list(map(int,input().split()))

    #Dem tan suat xuat hien cac phan tu trong mang
    cnt=[0]*(10000001)
    for i in range(len(a)):
        cnt[a[i]]+=1
    
    for i in range(len(a)):
        if cnt[a[i]] >=1:
            print(a[i],cnt[a[i]],sep=":")
            cnt[a[i]]=0
    
    cnt=[0]*10000001
    #Dem so phan tu khac nhau trong mang
    for i in range(n):
        cnt[i]=1
    l,r=min(a),max(a)
    res=0
    for i in range(l,r+1):
        if cnt[i]!=0:
            res+=1
    print(res)

