number = int(input())
f = 0
while number > 0:
    a = number % 10
    f = f + a
    number = number // 10
print(f)