#BAI 34: SO FIBONACCI

"""
so fibonacci: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34.....

- Baitoan: Kiem tra 1 so co phai so fibonacci khong, in ra so fibonacci thu n,
in ra n so fibobacci dau tien...vv

*Quy luat: 
     { 1 (n=1)
F(n)={ 1 (n=2)
     { F(n-1) + F(n-2) (n>2)
     
"""

#in ra n so fibonacci dau tien (0->n-1)
def fibo(n):
    print("0 1",end=" ")
    fn1,fn2=1,0     
    for i in range(2,n):
         fn=fn1+fn2
         print(fn,end=" ")
         fn1,fn2=fn,fn1

#kiem tra 1 so co phai la so fibonacci khong (ta duyet 92 so fibo dau tien roi so sanh voi n)
def checkFibo(n):
     if n==0 or n==1:
          return True
     fn1,fn2=1,0
     for i in range(2,92): 
          fn=fn1+fn2
          if n==fn:
               return True
          fn1,fn2=fn,fn1
     return False

#in ra so fibo thu n

def printFibo(n):
     if n==0 or n==1:
          return n
     fn1,fn2=1,0
     for i in range(2,n+1):
          fn=fn1+fn2
          fn1,fn2=fn,fn1
     return fn

if  __name__== "__main__":
     n=int(input())
     
     fibo(n)

     if(checkFibo(n)):
          print("YES")
     else:
          print("NO")
     
     print(printFibo(n))
