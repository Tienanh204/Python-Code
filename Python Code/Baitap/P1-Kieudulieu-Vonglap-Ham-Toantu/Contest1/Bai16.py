#a->z: 97-122
#ord(x): chuyen x tu ky tu -> ma ascll
#chr(x): chuyen x tuma ascll -> ky tu

s=input()

if s=="z" or s=="Z":
    print("a")
else:
    if s>="A" and s<="Z":
        print(chr(ord(s)+32+1))
    else:
        print(chr(ord(s)+1))
