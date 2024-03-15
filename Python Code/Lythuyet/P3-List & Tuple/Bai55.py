#BAI 55: COPY LIST VA LIST LAM THAM SO CHO HAM

#1. Copy list
a=[1,2,3,4]
b=a
print(a)
print(b)

print(id(a),id(b), sep=" ")
"""
NOTE:
- Thực chất mảng a, b là 1 vì chúng thao tác trên cùng một đối tượng
- Khi thay đổi a -> b cũng thay đổi và ngược lại

=> Vậy khi ta muốn tạo ra 1 bản sao của a thì ta phải dùng copy()
chứ không thể gán như trên
"""

b=a.copy() #-> luc nay a,b moi thuc su la 2 thang khac nhau
print(id(a),id(b), sep=" ")


#2. List lam tham so
def change(arr):
    arr[0]=1000
a=[1,2,3,4]
change(a)
print(a) #-> bi thay doi nha noi chung khac c++

