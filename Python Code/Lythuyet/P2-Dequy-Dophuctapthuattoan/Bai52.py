#BAI 52: DO PHUC TAP CUA THUAT TOAN

#1. Tinh toan do phuc tap cua thuat toan va ky hieu Bing O
"""
- Kí hiệu Big O mô tả trường hợp tệ nhất của thuật toán thông qua một hàm của input đầu vào n.
O(f(n)) = O(n), O(1), O(logn), O(nlogn), O(n^2), O(n!)...
- Neu: f(n) tang cang nhanh thi do phuc tap thuat toan cang cao
so phep toan thuc hien cang lon

"""

#a) O(1)
"""
- Code sau co do phuc tap thuat toan O(1):
a,b,c=100, 200, 300
sum=a+b+c
print(sum)
tich = a*b*c
print(tich)

NOTE: +, -, *, /, %, phep gan, so sanh, nhap xuat -> O(1)
"""

#b) O(n), O(n*can(n))
"""
VD1: 
for i in rane(n):
    print(i,end=" ")
-> O(n*1)=O(n)

VD2:
def nt(n):
    if n<2:
       return False
    for i in range(2, sqrt(n)+1):
       if n%i==0:
            return False
    return True

if __name__=="__main__":
   for i in range(n+1):
        if nt(i):
           print(i,end=" ")

-> O(n*can(n)) 

"""