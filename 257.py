gor1 = int(input())
vert1 = int(input())
gor2 = int(input())
vert2 = int(input())

if (gor1 + 2 == gor2 and (vert1 + 1 == vert2 or vert1 - 1 == vert2)) or (gor1 - 2 == gor2 and (vert1 + 1 == vert2 or vert1 - 1 == vert2)) or (gor1 + 1 == gor2 and (vert1 + 2 == vert2 or vert1 - 2 == vert2)) or (gor1 - 1 == gor2 and (vert1 - 2 == vert2 or vert1 + 2 == vert2)):
  print("YES")
else:
  print("NO")