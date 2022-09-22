a,b = map(int, input().split())

if a == 0 and b == 0:
    print("many solutions")
elif (a == 0 and b != 0) or b % a != 0:
    print("no solution")
else:
    print(b // a)