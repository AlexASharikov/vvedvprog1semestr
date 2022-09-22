a = int(input())
b = int(input())
c = int(input())

if a > b:
    if a > c:
        if b > c:
            print(c,b,a)
        else:
            print(b,c,a)
    else:
        print(b,a,c)
elif a < b:
    if a < c:
        if b < c:
            print(a,b,c)
        else:
            print(a,c,b)
    else:
        print(c,a,b)
