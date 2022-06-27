from sys import stdin

n, m = map(int, stdin.readline().split())
li = []
inlist=0
for i in range(0, n):
    li.append(stdin.readline())

for i in range(0, m):
    word = stdin.readline()
    if word in li:
        inlist+=1

print(inlist)
