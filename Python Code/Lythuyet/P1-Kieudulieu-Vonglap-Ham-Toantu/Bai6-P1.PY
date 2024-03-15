#BAI 6: NHAP DU LIEU TU BAN PHIM TRONG PYTHON

#1. Nhap du lieu voi ham input

"""
Cu phap: input(prompt)
-Gia tri tra ve: input() tra ve sxau ki tu o kieu str,
cac ban can chu y ep kieu sang du lieu tuong ung cua bien trong de bai
"""
#Cach 1: nhap du lieu tung dong
#input:
#100
#200
#300

s=input("Nhap so: ")
print("So vua nhap: ",s)
print(type(s),end="\n")

s=int(input("Nhap so: "))
print("So vua nhap: ",s)
print(type(s))


a=int(input("Chieu dai: "))
b=int(input("Chieu rong: "))
chuvi=2*(a+b)
dientich=a*b

print(chuvi,dientich,sep=" ")

#Cach 2: nhap du lieu tren cung 1 dong
#input: 100 200 300

"""
Cach lam:
B1: Nhap ca dong bang ham input
B2: Dung ham split de tach cac so trong xau input ra
B3: Su dung map de ep cac xau duoc tach ra trong input
sang so int hoac float tuy theo dau bai
"""

s=input("Nhap 3 so: ")
a=s.split() #a luc nay chua cac xau
x,y,z=map(int,a)#ep kieu xong gan cho x,y,z

x,y,x=map(int,input("nhap 3 so: ").split())# Tom lai cac buoc tren la dong lenh nay :> ben tren chi la gia thich ro rang tung buoc




