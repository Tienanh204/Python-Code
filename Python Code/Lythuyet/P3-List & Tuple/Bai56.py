#BAI 56: LIST SLICING (CẮT DANH SÁCH)

"""
- list slicing: giúp ta truy cập vào 1 khoảng các phần tử trong list
thông qua toán tử

- Sử dụng list slicing:
• Với toán tử: Bạn có thể xác định chỉ số bắt đầu, chỉ số kết thúc, bước
nhảy của các phần tử trong list mà bạn muốn cắt ra.
• Cú pháp: a[start, stop, step]. 

NOTE:
-> Nếu không có step thi mặc định là 1
-> Nếu cắt từ start - stop thi nó sẽ trả về đoạn [start,stop-1]
-> Nếu bỏ stop thì mặc định là chỉ số cuối cùng của mảng
-> Nếu bỏ start thì mặc định là chỉ số bắt đầu của mảng
"""
#1. Slicing voi chi so khong am
a=[1,2,3,4,5,6]
b=a[2 : 4+1 : 1] #-> cat ra doan [3,4,5]
print(b)

#2. Slicing voi chi so am
a=[1,2,3,4,5,6]

b=a[1:-2]
print(b)

c=a[-4:-1]
print(c)

#3. Lat nguoc list ***
"""
*NOTE: rất hay nha =))
- Để lật ngược list các bạn chỉ cần 
bỏ trống phần start và stop, phần step cho bằng -1
"""

a=[3,2,1,"Tien anh","Le tram"]
b=a[::-1]
print(b)

#4. Thay doi gia tri cua nhieu phan tu trong 1 doan

a=[1,2,3,4,5,6,7,8]
a[1:3]= [100,100] #Thay đổi đoạn [2,3]=[100,100]
a[1:3]=[] #Xóa đoạn [2,3]

print(a)

#5. Chen va xoa voi list slicing

a=["x","y","z"]
a[:0]=[10,20,30] #Them vao dau list
a[len(a):]=[10,20,30] #Them vao cuoi list
print(a)

#6. Copy mot list (deep copy)  ***

a=["x","y","z"]
b=a.copy() #cach lam thong thuong
b=a[:] #Dung slicing -> Rat hay nha

print(b)
print(a==b) 
print(b is a)