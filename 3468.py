var = int(input())
minutes = var % 60
hours = var // 60
while hours >= 24:
    hours = hours - 24
print(hours,minutes)