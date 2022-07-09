import sys

input = sys.stdin.readline
# print = sys.stdout.write

n, k = map(int, input().split())

li = [i for i in range(1, n+1)]
result = []
while(len(li) != 0):
    if len(li) == 1:
        p = li.pop(0)
        result.append(p)
        break
    for i in range(1, k):
        p = li.pop(0)
        li.append(p)
    result.append(li[0])
    li.pop(0)

print('<'+', '.join(map(str, result))+'>')
