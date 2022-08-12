import sys
input = sys.stdin.readline

n, m = map(int, input().split())
d = {}
for _ in range(n):
    addr, pw = input().split()

    d[addr] = pw

for _ in range(m):
    print(f'{d[input().strip()]}')
