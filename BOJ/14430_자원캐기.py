import sys
from copy import deepcopy as dc

input = sys.stdin.readline

n, m = map(int, input().split())

li = [ list(map(int, input().split())) for _ in range(n) ]
tmp = dc(li)

for col in range(1, m):
    tmp[0][col] += tmp[0][col-1]

for row in range(1, n):
    tmp[row][0] += tmp[row-1][0]

for i in range(1, n):
    for j in range(1, m):
            tmp[i][j] = max(tmp[i-1][j], tmp[i][j-1]) + li[i][j]

print(tmp[n-1][m-1])
            
