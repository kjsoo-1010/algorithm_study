import sys
input = sys.stdin.readline

n = int(input())
res = set()
for i in range(n):
    res.add(int(input()))
res = list(res)
res.sort()
for k in res:
    print(k)
