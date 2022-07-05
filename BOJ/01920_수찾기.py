import sys

input = sys.stdin.readline
print = sys.stdout.write

n = input()
A = set(map(int, input().split()))
m = input()
test = list(map(int, input().split()))

for t in test:
    if t in A:
        print('1\n')
    else:
        print('0\n')
