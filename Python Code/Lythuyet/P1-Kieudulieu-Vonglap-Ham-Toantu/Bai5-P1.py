#BAI 5: TOAN TU TRONG PYTHON

#1. Toan tu

#a. Toan tu gan "="
"""
Cu phap: a=b
-Gan gia tri cho nhieu bien trong cung 1 cau lenh: a,b,c=100,200,300
-Hoan vi gia tri cua 2 bien trong Python:
a=100
b=200
a,b=b,a

"""
a=100
b=a
print(b)

a,b,c=100,200,300
print(a,b,c)

a="28tech"
b="Tien anh"
a,b=b,a
print(a,b)

#b. Toan tu toan hoc
"""
+: Cong
-: Tru
*: Nhan
/: Chia
//: Chia nguyen
%: Chia du
**: Luy thua
"""
a=10
b=20
print(a+b,a-b,a*b,a/b,a//b,a**b,sep=" ")

#c. Toan tu so sanh
"""
==: So sanh bang
>: Lon hon
>=: Lon hon hoac bang
<: Nho hon
<=: Nho hon hoac bang
!=: Khac
"""

print(100<200)
print(100>200)

#d. Toan tu logic
"""
and: Toan tu va(dung khi tat ca cung dung con lai sai)
or: Toan tu hoac(sai khi tat ca cung sai con lai dung)
not: Toan tu phu dinh(sung la sai, sai la dung)
"""

#e. toan tu nhan dang
"""
Duoc su dung de so sanh 2 doi tuong chu khong phai so sanh 2 gia tri
is: Tra ve true neu 2 doi tuong la giong nhau
is not: Tra ve True neu 2 doi tuong la khac nhau
"""
a=[1,2,3]
b=[1,2,3]

print(a==b)
print(a is b)# kieu nhu 2 thang cung ten nhung no khong phai la nhau

#f. Toan tu thanh vien
"""
-Dung de kiem tra su ton tai cua 1 doi tuong trong list, xau, tuple...
in: Tra ve True neu doi tuong kiem tra ton tai (VD: 'a' in 'abcd'-->True)
not in: Tra ve True neu doi tuong kiem tra khong ton tai (VD: 'a' not in '28tech'-->True)
"""

s="Tien Anh, who is the most of beaty in the world"
t="who"
q="paraben"

print(t in s)
print(q not in s)
