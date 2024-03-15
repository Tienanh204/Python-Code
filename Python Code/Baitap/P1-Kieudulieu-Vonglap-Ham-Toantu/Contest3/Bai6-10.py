from math import*

#Bai6: Tong uoc so
def sum1(n):
    res=0
    for i in range(1,int(sqrt(n))+1):
        if n%i==0:
            res+=i
            if i!=n//i:
                res+=n//i
    return res


#Bai7: So chinh phuong (Da lam)


#Bai8: So chinh phuong trong doan
"""
- Duyet trau tu a->b roi lam nhu bai 6 thi lau va bị time limited,
nen ta dung cach sau:
a<=i^2<=b --> sqrt(a)<=i<=sqrt(b) #Note cai can duoi a nha
"""
def square(a,b):
    can1,can2=sqrt(a),sqrt(b)
    for i in range(ceil(can1),int(can2)+1):
        print(i*i,end=" ")


#Bai9: So chinh phuong 3 (Dem cac so chinh phuong trong doan [a,b]) -> Lam tuong tu bai 8
def square1(a,b):
    cnt=0
    for i in range(int(sqrt(a)),int(sqrt(b))+1):
        if(i*i>=a):
            cnt+=1
    return cnt
    

if __name__=="__main__":
    a,b=map(int,input().split())
    print(square1(a,b))
