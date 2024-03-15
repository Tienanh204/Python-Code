#BAI 19: VONG LAP FOR

#1. Vong lap for va ham range()
#a) Ham range():
"""
- Ham range() se sinh ra mot day so va ban se su dung
vong for de duyet qua tung so trong day da sinh ra

*Cu phap:
range(start, stop, step)

trong do:
.start: Gia tri bat dau cua day so (mac dinh la 0)
.stop: gia tri cuoi cung cua day so (can nay khong duoc lay)
.step: Buoc nhay cua day so (mac dinh la 1)
"""

a=range(1,10,1)
b=range(10)

for i in a:
    print(i,end=" ")#--> in ra [1,9]

for i in b:
     print(i,end=" ")#--> in ra [0,9]

#b) Vong lap for

#in ra cac so tu 1 -> 50 (noi chung tuy vao yeu cau de bai minh tuy chinh start, stop, step cho hop ly)

for i in range(1,50):
     print(i,end=" ")

for i in range(10,0,-1):
     print(i,end=" ")
    
"""
Lay tung thang o trong range() gan cho i qua moi vong lap
"""
for i in range(7):
     print(i,end="\n") #--> in ra [1,6], ta phai hieu la no lay tung gia tri trong range()
     i+=1             # gan cho i nen thay doi nhu kia cha anh huong gi het du i+=1000..



#2. Cau lenh break va continue
"""
- Tinh chat y chang ben cach ngon ngu khac
"""
#a) Vong for long nhau
n,m=3,2

for i in range(n+1):
     for j in range(m+1):
          print(i,j)