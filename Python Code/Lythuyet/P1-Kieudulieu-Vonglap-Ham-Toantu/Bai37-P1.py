#BAI 27: LY THUYET DONG DU

"""
Hiệu suất tính toán: Khi bạn làm việc với các số nguyên lớn,
việc thực hiện các phép toán như cộng, trừ, nhân có thể gây ra sự tràn số hoặc dẫn đến yêu cầu lưu trữ rất lớn.
Bằng cách sử dụng đồng dư, bạn có thể giới hạn kích thước của các số tham gia vào phép toán và giảm nguy cơ tràn số.
Tuy nhiên trong Python thì nó cho phép lưu trữ dữ liệu rất lớn nhưng C++/C/Java thì không được như thế,
nên ta phải học lý thuyết đồng dư là vậy :>


* Ly thuyet dong du: +, -, *, /

. (A + B) % C=((A % C) + (B % C)) % C
. (A - B) % C=((A % C) - (B % C) + C) % C
. (A * B) % C=((A % C) * (B % C)) % C
. (A / B) % C=((A % C) * (B^-1 % C)) % C

"""
from math import*

#baitoan: Tinh N! chia du cho 10^9+7

if __name__=="__main__":
    n=int(input())

    #baitoan1: Tinh N! chia du cho 10^9+7

    #cach lam thong thuong, nhung neu n la so cuc lon thi no se tinh rat lau
    res=factorial(n)
    print(res % (10**9+7))
    
    #n!=[n*(n-1)*....1] % mod -> dung phep nhan toi dau chia du toi do nen la so no se rat nho va de xu ly
    res=1
    for i in range(1,n+1):
        res*=i
        res%=(10**9+7)
    print(res)

    #baitoan2: Tinh a^b chia du cho c
    a,b,c=map(int,input().split())
    res=1

    for i in range(1,b+1):
        res*=a
        res%=c
    print(res)

"""
NOTE: kể từ giờ về sau khi bài toán yêu cẩu chia dư kết quả
cho một số nào đó => Tính đến đâu chia dư đến đó :3 nhớ nha
"""
