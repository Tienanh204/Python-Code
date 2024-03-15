#BAI 46: DE QUY (RECURSION)

#1. Cau truc du lieu ngan xep
"""
-   Ngan xep la 1 CTDL ho tro 2 thao tac push pop.
Trong do push giup them 1 phan tu vao ngan xep, pop giup xoa
1 phan tu khoi dinh ngan xep. Ca 2 thao tac nay deu duoc thuc hien
o dinh ngan xep
"""

#2. Stackframe la gi?
"""
- Những thành phần của stack frame
có thể kể đến như biến cục bộ, đối số, địa
chỉ trả về của một chương trình con

- Mỗi khi lời gọi hàm được thực hiện,
stack frame chứa thông tin của hàm đó 
được đẩy và bộ nhớ stack và khi hàm
đó kết thúc thì stack frame này được 
loại khỏi bộ nhớ stack

vd:
def A():
    print("A)

def B():
    A() #goi ham A
    print("B)

|     |                                           |     |                                           |   |
| A() |  -> print("A"),sau khi ham A chay xong -> |     | -> print("B"), sau khi ham B chay xong -> |   | -> ket thuc chuong trinh
|_B()_|     no se bi xoa khoi stack               |_B()_|    no cung se bi xoa khoi stack           |___|


"""

#3. Ham de quy
"""
- Ham de quy la mot ham goi lai chinh no

vd1:
def A():
    print("A")
    A() #De quy

vd2:
def S(n):
    if n==0:
       return 0
    else:
       return n + S(n-1) #De quy

if __name__=="__main__":
    n=4
    print(S(4)) --> KQ: 10

Giai thich:

|      |              |      |               |      |                  |      |                  | S(0) | = 0
|      |              |      |               |      |                  | S(1) | = 1 + s(0)       | S(1) |
|      |       ->     |      |          ->   | S(2) | = 2 + s(1) ->    | S(2) |            ->    | S(2) |
|      |              | S(3) | = 3 + S(2)    | S(3) |                  | S(3) |                  | S(3) |
|_S(4)_| = 4 + S(3)   |_S(4)_|               |_S(4)_|                  |_S(4)_|                  |_S(4)_|
                                                                       
                                                                                                    | (Ham S(0) ket thuc,
                                                                                                    | va day khoi stack)
                                                                                                    V
|      |       |      |             |      |                 |      |                            |      | 
|      |       |      |             |      |                 |      |                            | S(1) | = 1 + s(0) = 1
|      |  <-   |      |        <-   |      |           <-    | S(2) | = 2+S(1) =3,  s(1)  <-     | S(2) |
|      |       |      |             | S(3) | = 3+S(2)=6      | S(3) |               ket thuc     | S(3) |
|______|       |_S(4)_| = 4+S(3)=10 |_S(4)_|                 |_S(4)_|               bi day ra    |_S(4)_|

NOTE: cái việc S(i) = x + S(i-1) như trên là tượng trưng thôi nhá thật ra sub ra là hàm S(i) return về giá trị x+S(i-1)
*Một bài đệ quy bao gồm:

+ Bài toán con nhỏ nhất -> (Điểm dừng của lời gọi đệ quy vd: if n==0: return 0)

+ Công thức truy hồi -> (Tổng hợp kết quả của bài toán lớn thông qua bài toán  
                         con đã biết đáp án vd: S(n)=n+S(n-1), sau khi lời đệ quy lần tới bài toán con nhỏ nhất S(0) thì sau đó nó lần ngược lại tính S(1)->...->S(4) )

                         
"""
