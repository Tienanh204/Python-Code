#BAI 4: BIEN VA KIEU DU LIEU TRONG PYTHON | EP KIEU

#1. Bien va kieu du lieu
#a. Bien
a=100
b="28Tech"
c=30.25
print(type(a),type(b),type(c))# in ra kieu du lieu cua moi bien

"""
Cach dat ten bien:
1. Khong co dau cach trong ten VD: dien tich=10
2. Khong bat dau bang so VD: 100a=2
3. Khong dat ten bien chua dau ky tu dac biet VD: & # @ !...vv
4. Ten bien trong Python phan biet chua hoa va chu thuong VD: hi=100, Hi=200 la 2 bien khac nhau
"""

#b. Kieu du lieu
#kieu du lieu so

"""
<class 'int'> : Kieu du lieu so nguyen
-Khong gioi han gia tri so nguyen co the luu --> ngon ngay
-Doi voi so nguyen ta co the gan va in ra cac co so o he: 2 8 16
VD: 
a=0b1101
b=13
print(a,b)-> ket qua a=b=13
"""
a=0b1101
b=13
print(a,b)

"""
<class 'float'>: kieu du lieu dau so thuc
-Khac voi so nguyen thi so thuc se bi gioi han ve gia tri luu
[5.0*10^-324, 1.8*10^308]
value > 1.8*10^308: ket qua in ra la inf (vo cung)
value < 5.0*10^-324: ket qua in ra la 0

-Cach in so luong chu so sau dau phay xac dinh
VD: a=28.0412323
co 3 cach in ra voi ket qua lay 2 so sau day phay--> output: 28.04
c1: print("%.2f" % a)
c2: print(round(a,2))
c3: ("{:.2f}".format(a))

"""
a=28.04122323
print("%.2f"%a)
print("{:.4f}".format(a))

"""
<class 'complex'>: Kieu du lieu so phuc
a+bj
a: phan thuc->real
b: phan ao->imag
"""
a=3+5j
print(a.real)
print(a.imag)

#Kieu du lieu dung sai
"""
-Kieu bool chi luu 2 gia tri True or False
-Note: cac gia tri duoc xac dinh la Truie trong python (xau khac rong, cac so khac 0)

"""

a=True
b=False
print(type(a),type(b))

a=100
b=0
c="Tien anh"
d=""
print(bool(a),bool(b),bool(c),bool(d))

#Kieu du lieu xau ky tu(str)
"""
-Xau ky tu duoc dat trong dau nhay don hoac nhay kep tren 1 dong trong truong hop nhieu dong ta dat giua 3 dau nhay kep
"""

s="28tech"
q='28tech'
t="""Neu nuoc mat troi di
bao nhieu yeu thuong tinhg cu mai xa"""

print(s)
print(q)
print(t)

#2.Ep kieu
"""
int(): Ep kieu sang so nguyen
"""
s="123"
a=int(s)#ep tu str->int
print(type(a))

s=20.1567
a=int(s)
print(a)#in ra mat phan thap phan

"""
str(): Ep kieu sang xau
foat(): Ep kieu sang so thuc
...vv
"""
