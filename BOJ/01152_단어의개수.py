line = input().split(' ')
length = len(line)
sum = 0

while ('' in line):
    idx = line.index('')
    sum += 1
    line = line[idx:]
    line.remove('')

print(length - sum)
