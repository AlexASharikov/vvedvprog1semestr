gor1,vert1,gor2,vert2 = map(int, input().split())

if gor1 == gor2 or vert1 == vert2 or abs(gor1 - gor2) == abs(vert1 - vert2):
  print("YES")
else:
  print("NO")