import sys

input = sys.stdin.readline
print = sys.stdout.write

dic = {}
for _ in range(int(input())):
    x, y = map(int, input().split())
    if x in dic:
        dic[x].append(y)
    else:
        dic[x] = [y]

xx = list(dic.keys())
xx.sort()

for x in xx:
    yy = dic[x]
    yy.sort()
    for y in yy:
        print(f'{x} {y}\n')
