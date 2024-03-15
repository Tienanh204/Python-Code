#BAI 29: KIEM TRA SO NGUYEN TO

from math import*

def check1(n):#code trau
    if n<2: return False
    for i in range(2,n):
        if(n%i==0):
            return False
    return True

def check2(n):#code toi uu
    if n<2: return False
    for i in range(2,int(sqrt(n))+1):
        if(n%i==0):
            return False
    return True

if __name__=="__main__":
    n=int(input())
    if(check1(n)):
        print("YES")
    else:
        print("NO")
    
    if(check2(n)):
        print("YES")
    else:
        print("NO")