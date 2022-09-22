gor1 = int(input())
vert1 = int(input())
gor2 = int(input())
vert2 = int(input())

if gor1 == gor2 or vert1 == vert2 or abs(gor1 - gor2) == abs(vert1 - vert2):
  print("YES")
else:
  print("NO")