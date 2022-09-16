a,b,c = map(int, input().split())
summa = a + b + c
proizv = a * b * c
sredarif = (a + b + c)/3
print(a,"+",b,"+",c,"=",summa, sep="")
print(a,"*",b,"*",c,"=",proizv, sep="")
print("(",a,"+",b,"+",c,")/3=",f"{sredarif:.3f}", sep="")