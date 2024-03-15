#BAI 58: LIST COMPREHENSION
from math import*
"""
- Comprehension là một cách nhanh chóng để có thể tạo ra một cái list
từ 1 cái iterable. Nó có thể kết hợp với điều kiện và vòng lặp để rút gọn
cú pháp. List comprehension sẽ giúp code của bạn Pythonic hơn
"""

a=[1,2,3,4,5,6,7,8]
b=[]
for x in a: #cach thong thuong hoi dai --> dung list comprehension cho ngan gon
    if x%2==0:
        b.append(x)
print(b)



#1. Cu phap va cac vi du co ban
"""
*Cu phap:
[Expression for var in iterable]

Trong đó:
• Expression: Biểu thức được thực hiện mỗi khi vòng lặp thực thi.
• Var: Một biến là một item trong iterable.
• Iterable: Collections chứa các object (list, tuple, str...)
"""

a=["java","python","C++"]
b=[x for x in a] #copy tu a sang b
print(b)

a=[1,2,3,4]
b=[x**2 for x in a]#binh phuong phan tu trong a -> b
print(b)

b=[x**2 for x in range(5)]
print(b)


def sum_digit(n):
    tong=0
    while(n!=0):
        tong+=n%10
        n//=10
    return tong
a=[1,233,30,4,99,13,123]
b=[sum_digit(x) for x in a]
print(b)

#2. list comprehension voi cau lenh if

"""
- Khi sử dụng dữ liệu list comprehension bạn cso thể sử dụng
mệnh đề if để lọc dữ liệu phù hợp

*Cú pháp:
[Expression for var in iterable if_clause]
"""
def nto(n):
    if n<2: return False
    for i in range(2,int(sqrt(n))+1):
        if n%i==0:
            return False
    return True

a=[1,-2,3,-4,5,-6]
b=[x for x in a if x>0]
print(b)

n=10
a=[x for x in range(n) if x%2==0]
print(a)

a=[x for x in range(n) if nto(x)]
print(a)


#3. Nested List comprehension
"""
- Biểu thức bên trong list comprehension có thể là một list comprehension khác

"""
