#BAI 57: HAM LAMBDA

#1. Lambda la gi?
"""
- Lambda là một cách đơn giản để định nghĩa hàm trong Python
- Lambda là một cách để định nghĩa hàm vô danh, một hàm mà không cần tên hàm. Nó được sử dụng
khi bạn cần xây dựng những hàm chỉ bao gồm 1 câu lệnh -> Thì ta sài luôn lambda cho nó lẹ :))

*Cú pháp:
lambda parameters: expression

"""

def func(n): #Xay dung ham
    return 2*n
print(func(10))
print(func(20))

func = lambda x: x*2 #Su dung lambda (Ta thay vi ham tren o 1 cau lenh nen ta dunfg lambda cho nhanh)
print(func(10))
print(func(20))


#2. Cac tinh chat cua lambda
"""
• Lambda không thể chứa các câu lệnh: Ví dụ như return, assest, pass...
• Lambda chỉ chứa 1 biểu thức duy nhất.
• IIFE : Immediately Invoked Function Expression: Biểu thức lambda có
thể được gọi ngay lập tức
"""
res=(lambda x: x**2)(10)
print(res)

func=lambda x,y,z: x+y+z
print(func(1,2,3))

#3. Lambda ket hop voi map() or filter
"""
- Hàm map() trong Python có 2 đối số
là một hàm và 1 list, map áp dụng
hàm này với các phần tử trong list.

- Hàm filter() tương tự như hàm map, khi
apply các hàm trong filter với từng phần tử
trong list mà giá trị của hàm trả về True thì
filter lọc ra các phần tử này.
"""
a=[1,2,3,4,5]
b=list(map(lambda x : x**2, a))
print(b)

b=list(filter(lambda x: x%2==0,a))
print(b)

#4. if else va lambda
"""
- Có thể kết hợp if else vào trong lambda
"""
finmax = lambda x,y : x if x>y else y
print(finmax(100,200))
