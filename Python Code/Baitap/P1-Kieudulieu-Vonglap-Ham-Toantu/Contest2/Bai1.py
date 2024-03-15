n=int(input())

#FOR
for i in range(1,n+1):
    print(i,end=" ")
print("\n")

for i in range(n,-1,-1):
    print(i,end=" ")
print("\n")

for i in range(n+1):
    if(i%2==0):
        print(i,end=" ")
print("\n")

for i in range(n+1):
    if(i%2!=0):
        print(i,end=" ")
print("\n")

for i in range(n):
    if(i%4==0):
        print(i,end=" ")
print("\n")

x=97;
for i in range(n):
    print(chr(x),end=" ")
    x+=1
print("\n")

x=122-n+1
for i in range(n):
    print(chr(x),end=" ")
    x+=1
print("\n")

#WHILE
i=1
while i<=n:
    print(i,end=" ")
    i+=1
print("\n")

i=n
while i>=0:
   print(i,end=" ")
   i-=1
print("\n")

i=0
while i<=n:
    if(i%2==0):
        print(i,end=" ")
    i+=1
print("\n")

i=0
while i<=n:
    if(i%2!=0):
        print(i,end=" ")
    i+=1
print("\n")

i=0
while(i<n):
    if(i%4==0):
        print(i,end=" ")
    i+=1
print("\n")

x=97
i=0
while i<n:
    print(chr(x),end=" ")
    x+=1
    i+=1
print("\n")

x=122-n+1
i=0
while(i<n):
    print(chr(x),end=" ")
    x+=1
    i+=1