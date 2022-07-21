import sys

input = sys.stdin.readline
print = sys.stdout.write

n, k = map(int, input().split())
move = k
cnt = 0
while(True):
    if move%2 == 0:
        move = move//2
    else:
        move -= 1
    cnt += 1
    

    if move <= n and n < move * 2:
        break

cnt += abs(move-n)

print(f'{cnt}')
