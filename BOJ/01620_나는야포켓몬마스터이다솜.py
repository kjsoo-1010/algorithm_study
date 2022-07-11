import sys

input = sys.stdin.readline
print = sys.stdout.write

n, m = map(int, input().split())
numKey = {}
pocketmonKey = {}

for i in range(1, n+1):
    name = input().strip()
    numKey[i] = name
    pocketmonKey[name] = i

for _ in range(m):
    q = input().strip()
    try:
        print(f'{numKey[int(q)]}\n')
    except:
        print(f'{pocketmonKey[q]}\n')
