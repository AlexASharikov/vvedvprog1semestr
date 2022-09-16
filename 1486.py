number = int(input())
a = number % 10
number = number // 10
b = number % 10
number = number // 10
c = number % 10
number = number // 10
d = number % 10
Num1 = 1 // (abs(a - b) + 1) + 1 // (abs(a - c) + 1) + 1 // (abs(a - d) + 1)
Num2 = 1 // (abs(b - c) + 1) + 1 // (abs(b - d) + 1) + 1 // (abs(c - d) + 1)
print(Num1 + Num2)