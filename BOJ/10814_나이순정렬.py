dic = {}
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    age, name = input().split()
    age = int(age)

    if age in dic:
        dic[age].append(name)
    else:
        dic[age] = [name]

ages = list(dic.keys())
ages.sort()

for a in ages:
    for name in dic[a]:
        print(a, name)
