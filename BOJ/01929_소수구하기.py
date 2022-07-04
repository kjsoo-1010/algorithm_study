import sys
input = sys.stdin.readline
print = sys.stdout.write

# import time

first, second = map(int, input().split())
# start = time.time()

li = []

def prime(m):
    tmp = ''
    if m == 2:
        li.append(2)
    else:
        for l in li:
            if l > int(m**(1/2)):
                break
            if m % l == 0:
                tmp = 'BREAK'
                break
        if tmp != 'BREAK':
            li.append(m)


for i in range(2, second+1):
    if i<2:
        pass
    else:
        prime(i)

for l in li:
    if l < first:
        pass
    else:
        print(f'{l}\n')
