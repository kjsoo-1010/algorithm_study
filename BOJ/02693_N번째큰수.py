n = int(input())
for i in range(0, n):
  l = list(map(int, input().split()))
  l.sort(reverse=True)
  print(l[2])
