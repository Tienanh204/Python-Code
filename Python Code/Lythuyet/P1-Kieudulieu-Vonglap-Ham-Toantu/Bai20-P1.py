#BAI 20: VONG LAP WHILE VA CAC BAI TOAN UNG DUNG

#a) Vong lap while, break, continue

"""
*Cu phap: 
while condition:
      #code when condition is True
else:
      #code when condition is False

"""

n=1
while(n<=5):
    print("Yeu em den khi tac tho")
    n+=1

#bai toan: yeu cau nguowi dung nhap vao so duong, nhap so am hoac 0 thi bat nhap lai
while True:
    n=int(input())
    if(n<=0):
        print("N khong hop le, hay nhap lai")
    else:
        break
#bai toan: lat nguoc so n

n=1234
lat=0;
while n!=0:
   lat=lat*10+n%10
   n//=10
print(lat)