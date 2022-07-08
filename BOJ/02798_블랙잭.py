import sys

input = sys.stdin.readline

n, m = map(int, input().split())

cards = list(map(int, input().split()))

sub = 99999999999
total = 0

for i in range(0, n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            tmp = m - (cards[i] + cards[j] + cards[k])
            if tmp < sub and tmp >= 0:
                sub = tmp
                total = cards[i] + cards[j] + cards[k]
                # print(f'{i}, {j}, {k}')
print(total)
