print("ax^2 + bx + c = 0")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

D = b*b - 4*a*c
if D > 0:
    solf = (-b + D ** 0.5) / (2 * a)
    sols = (-b - D ** 0.5) / (2 * a)
    print(solf)
    print(sols)
elif D == 0:
    sol = (-b) / (2 * a)
    print(sol)
else:
    print("Нет корней")