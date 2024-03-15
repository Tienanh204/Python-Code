#BAI 27: HAM TRONG PYTHON

#1. Xay dung ham
"""
- De xay dung ham ta su dung tu khoa "def", truoc khi
xay dung ham can xac dinh cac tham so(gia tri ma
ban truyen cho ham), cau lenh return neu mong
muon tra ve gia tri nao do.

- Ham chi duoc chay khi no duoc goi

*Cu phap:
def function_name(paremeter):
    #code

Note: 
. Trong Python bien thi khong can kieu du lieu, nen
khi minh tra ve gia tri nao do thi tu khac no se nhan biet
kieu du lieu tra ve
. neu minh khong return thi ham no van tra ve 1 cai gia tri
la "None"

"""

def tong(a,b):
    res=a+b
    return res
m,n=10,20
print(tong(m,n))#--> KQ: 30


def xinchao(name1,name2):
    name1,name2="Tien Anh","Thanh Huong"

name1,name2=" "," "
print(xinchao(name1,name2))#--> KQ: None

"""
- Thong thuong cac ngon ngu lap trinh khac se co
ham "main" de xu ly code trong do nhung doi voi Python
thi khong co nen ta se thay bang:

*Cuphap:
if  __name__ == "__main__" :
    #Code

--> MUC DICH: cha qua de cho no nhin code de hieu va khoa hoc hon thoi
chu khoi can cung duoc, uu tien nen co nha:3
"""

def tong(a,b):
    return a+b

if __name__=="__main__":
    x,y=map(int,input().split())
    print(tong(x,y))

#2. keyword argument

def hello(name1,name2,name3):
    print("Xin chao", name1, name2, name3)

if __name__=="__main__":
    hello("Nam","Teo","Ty") #Positional argument
    hello(name3="Ty",name2="Teo",name1="Nam") #keyword argument

#3. default argument
"""
- Ban co the chi dinh cac gia tri mac dinh cho cac doi so khi
xay dung mot ham. Gia tri mac dinh duoc su dung neu ham
duoc goi ma khong co doi so tuong ung
"""

def infor(name,job="Di"):
    print(name,job)

if __name__=="__main__":
    infor("Tien anh","giam doc") #--> output: Tien anh giam doc
    infor("Tien anh") #--> output: Tien anh Di (Default argument)

