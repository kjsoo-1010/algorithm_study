import sys

input = sys.stdin.readline
print = sys.stdout.write

dic = {}
for _ in range(int(input())):
    x, y = map(int, input().split())
    if y in dic:
        dic[y].append(x)
    else:
        dic[y] = [x]

dic_y = list(dic.keys())
dic_y.sort()

for y in dic_y:
    dic_x = list(dic[y])
    dic_x.sort()
    for x in dic_x:
        print(f'{x} {y}\n')
