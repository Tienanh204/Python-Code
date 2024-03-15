#BAI 54: LY THUYAT VE LIST TRONG PYTHON

"""
- List tương tự như cấu trúc dữ liệu mảng 1 chieu ở các
ngôn ngữ lập trình khác nhưng có phần linh hoạt
và mạnh mẽ hơn.

- Cac tinh chat cua List
• Lists are ordered: Các phần tử trong list là có thứ tự.
• Accessed by index: Truy cập các phần tử trong list thông qua chỉ số.
• Lists can contain any sort of object: List có thể chứa các object thuộc
kiểu dữ liệu khác nhau như int, str, float, thậm chí là một list khác.
• Lists are changeable (mutable): Các phần tử trong list có thể thay đổi
giá trị, các thao tác thêm, xóa các phần tử cũng được hỗ trợ.
"""

#1. Tao List
"""
-List các số nguyên
a = [1, 2, 3, 4]

-List các xâu kí tự
b = ["28tech", "python", "ML"]

-List các số nguyên, xâu kí tự, số phức...
c = [1, 2, 3, 4, "Javascript", 3 + 5j]

-List rỗng
d = []
"""
#2. List constructor
"""
- Có thể sử dụng hàm list() để biến đổi các đối tượng khác thành list()
"""
s="Tien anh"
a=list(s)
b=list(range(10))

#3. Ham len()
"""
- Để biết số lượng phần tử trong list ta sử dụng hàm len().

a = [1, 2, 3, 4, "python", "28tech"]
print(len(a)) -> KQ: 6
"""

#4. Truy cap phan tu thong qua chi so

"""
- Chỉ số các phần tử trong list được đánh số từ 0 tính từ trái qua phải,
ngoài ra Python list hỗ trợ cả chỉ số âm.

chi so:     0  1  2  3  4
mang a:     2  2  7  6  3
chi so am: -5 -4 -3 -2 -1

NOTE: Chú ý truy cập vào chỉ số hợp lệ không là sẽ gây ra lỗi
"""


#5. Duyet List
#a) Duyet thong qua chi o
a=[1, 2, 3, 4, 5]
for i in range(0,len(a)):
    print(a[i],end=" ")

print()
for i in range(len(a)-1,-1,-1):
    print(a[i],end=" ")
print()

#b) Dung for each
a=[1, 2, 3, 4, 5]
for item in a:
    print(item,end=" ")



#6. Thay doi gia tri phan tu
a=[1, 2, 3, 4, 5]
a[2]="28teh" # 3->28tech
print(a)
print()

#7. Them phan tu vao trong list
"""
append(): Thêm một phần tử mới vào cuối list
insert(): Thêm một phần tử vào vị trí bất kì trong list
"""

a=[1, 2, "Tien anh", 4]
a.append("C++")
a.append("D++")
print(a)
print()

a.insert(1,"Facebook")
print(a)

#8. Xoa phan tu khoi list
"""
pop(): Xóa phần tử khỏi list thông qua chỉ số, nếu không chuyển chỉ
số cho hàm pop() nó sẽ xóa phần tử cuối cùng

del: Tương tự như hàm pop() -> dùng khi bạn không muốn lấy phần tử bị xóa đó

remove(): Xóa phần tử khỏi list thông qua giá trị (nếu trong list có nhiều phần tử giống nhau
nó sẽ xóa thằng đầu tiên) -> Note: nếu thằng muốn xóa không có trong list sẽ gây ra lỗi

clear(): Xóa mọi phần tử trong list
"""

#9. Sao chep list
"""
- Sao chép list có thể giúp bạn nhân bản nội dung
của 1 list ban đầu

vd1:
a=[1, 2, 3]
b=a*2
print(b) -> KQ: [1,2,3,1,2,3]

vd2:
a=[0]*1000
print(a) -> KQ: tạo ra 1 list chứa 1000 số 0
"""

#10. Tim kiem phan tu trong list
"""
- Để tìm kiếm phần tử trong list ta co thể dùng:
in hoặc thuật toán tìm kiếm tuyến tính -> cả 2 đều có độ phức tạp O(N)

"""
a=[1, 2, 3, 4, 5]

if 5 in a: # tim kiem bang in -> ban chat truy cap tung phan tu trong a roi so sanh
    print("YES")
else:
    print("NO")

def linear_search(a,x): # tim kiem tuyen tinh
    for iterm in a:
        if x==item:
            return True
    return False

"""
NOTE: bản chất tìm kiếm bằng in hay tuyến tính nó là như nhau
nên là 2 cách tìm kiếm bên trên đều hoạt động như nhau -> O(N)
"""

a=[1, 2, 3, 4]
b=[4, 5, 6, 7]

for i in range(len(b)): # Do phuc tap O(N^2) -> vi for + in
    if b[i] in a:
        print(b[i])


#11. Combine list
"""
extend(): Thêm các phần tử của 1 list khác vào list hiện tại
hoặc sử dụng toán tử +
"""
a=[1, 2, 3]
b=[4, 5, 6]

a.extend(b)
print(a)
print()
a+=b
print(a)

#12. Cac phuong thuc cua list
"""
a) Hàm copy(): Trả về một list mới có nội dung tương tự
như list ban đầu nhứng không phải list ban đầu

b) Hàm count(): Trả về số lần xuát hiện của phần tử

c) Hàm reverse(): Lật ngược 1 list


d) Hàm sort(): Sắp xếp các phần tử trong list

"""