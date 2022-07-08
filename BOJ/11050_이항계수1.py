import sys

input = sys.stdin.readline
print = sys.stdout.write

n, k = map(int, input().split())
if k > n//2:
    k = n - k

first, second = 1, 1

for i in range(k):
    first *= (n-i)
    second *= (k-i)

print(str(int(first / second)))
