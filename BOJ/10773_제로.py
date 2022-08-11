import sys

input = sys.stdin.readline
q = []
for _ in range(int(input())):
    n = int(input())
    if n == 0:
        q.pop()
    else:
        q.append(n)
print(sum(q))
