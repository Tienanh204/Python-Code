from  math import*

#Bai26: Fibonacci 1
def fibo1(n):
    print("1")
    fn1,fn2=1,0
    for i in range(2,n+1):
        fn=fn1+fn2
        print(fn)
        fn1,fn2=fn,fn1


#Bai26: Fibonacci 2
def fibo2(n):
    if n==0 or n==1:
        return True
    fn1,fn2=1,0
    for i in range(2,93):
        fn=fn1+fn2
        if n==fn:
            return True
        fn1,fn2=fn,fn1
    return False
    
if __name__=="__main__":
    n=int(input())
    if fibo2(n):
        print("YES")
    else:
        print("NO")