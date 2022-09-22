a = int(input())
b = int(input())
c = int(input())

if a > b:
    if a > c:
        if b > c:
            k = c
            l = b
            m = a
        else:
            k = b
            l = c
            m = a
    else:
        k = b
        l = a
        m = c
elif a < b:
    if a < c:
        if b < c:
            k = a
            l = b
            m = c
        else:
            k = a
            l = c
            m = b
    else:
        k = c
        l = a
        m = b
print(k,l,m)

