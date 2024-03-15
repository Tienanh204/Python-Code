from math import*

#Bai11: Chuyen he thap phan sang he nhi phan
def stran2to10(n):
    if n!=0:
        stran2to10(n//2) #gam con truy nguoc lai de tinh stran2to10(19)-> no se bat dau tu dong nay tro xuong 
        print(n%2,end="")

#Bai12: huyen he thap phan sang he 16
def stran10to16(n):
    if n!=0:
        stran10to16(n//16)
        if n%16 >=10 and  n%16 <=15:
            print(chr(n%16+55),end="")
        else:
            print(n%16,end="")

#Bai13: Tinh tong chu so cua N su dung de quy
def sumN(n):
    if n<10:
        return n
    return n%10+sumN(n//10)

if __name__=="__main__":
    n=int(input())
    print(sumN(n))