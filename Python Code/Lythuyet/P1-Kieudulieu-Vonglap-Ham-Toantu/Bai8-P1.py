#BAI 8: CAU TRUC RE NHANH ELSE IF TRONG PYTHON

#1. if va mot so vi du ve if
"""
- if duoc su dung khi ban can kiem tra dieu kien nao do
truoc khi thuc hien mot hoac nhieu cau lenh. Cac cau
lenh ben trong if duoc thut le so voi if.

*Cu phap: 
if condition:
    #code

- Ta co the su dung (and,or,not) de ket hop nhieu dieu kien voi nhau

"""

if 10<20:
    print("28tech")
    print("Programing")

n=10
if n<20 and n>5:
    print("YES")

if n%2==0:
    print("So chan")

#2. else va mot so vi du va else
"""
- Duoc su dung trong truong hop condition ben trong if la sai

*Cu phap
if condition:
   #code if condition if True
else:
   #code if condition is false
 
"""

n=11
if n%2==0:
    print("So chan")
else:
    print("So le")

n=30
if n%3==0 and n%5==0:
    print("Chia het")
else:
    print("Khong chia het")

#3. elif va mot so vi du ve elif
"""
- Tu khoa elif (else if) trong python duoc su dung ben duoi if
de kiem tra them dieu kien bo sung neu dieu kien ben tren sai
cac dieu kien o ben trong if va elif neu dung thi khoi code 
tuong ung se duoc thuc thi, neu khong co dieu kien nao 
dung thi khoi lenh ben trong else duoc thuc thi

*Cu phap
if condition1:
   #code1
elif condition2:
   #code2
......
elif condition3:
   #codeN
else
   #codeElse

"""

a,b=100,200
if a<b:
    print(a,"nho hon",b)
elif a>b:
    print(a,"lon hon",b)
else:
    print(a,"bang",b)


t=3

if t==1 or t==3 or t==5 or t==7 or t==8 or t==10 or t==12:
    print("31 ngay")

elif t==4 or t==6 or t==9 or t==11:
    print("30 ngay")
else:
    print("28 ngay")

#4. Shorthand if va toan tu ba ngoi

"""
- Ban co the su dung cau lenh if tren 1 dong
NOTE: NEN DUNG CAI NI CHO NHANH GON :)))
"""
a,b=100,200
if a<b: print(a,"nho hon",b)

#5. if long nhau
"""
Khi dieu kien trong if qua phuc tap, ban co the su dung
if long nhau (nested if) de kiem tra tung dieu kien mot
"""

#Kiem tra xem n co phai la so >= 50 va chia het cho 1 trong 3 so : 3,5,7

n=80
if n>=50:
    if n%3==0 or n%5==0 or n%7==0:
       print("YES")
    else:
        print("NO")
else:
    print("NO")