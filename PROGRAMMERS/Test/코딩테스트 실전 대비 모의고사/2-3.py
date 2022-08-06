'''
class Node:

    def __init__(self, item):
        self.data = item
        self.parent = []
        self.child = []

    def depth(self):
        M = 
        for node in self.parent:
            
            

tree = Tree()
'''

# n = 5
# roads = [[1, 2], [1, 4], [2, 4], [2, 5], [4, 5]]
# sources = [1, 3, 5]
# destination = 5

n = 3
roads = [[1, 2], [2, 3]]
sources = [2,3]
destination = 1

li = [0] + ([999999] * n)
d = {}
for road in roads:
    first, second = road[0], road[1]
    if first == destination:
        first = 0
    elif second == destination:
        second = 0

    if first > second :
        first, second = second, first
        
    if first in d:
        d[first].append(second)
    else:
        d[first] = [second]

k = list(d.keys())
k.sort()

for node in d[0]:
    li[node] = 1

for key in k:
    if key != 0:
        for value in d[key]:
            print(key, value)
            li[key] = min(li[value] + 1, li[key])
            li[value] = min(li[value], li[key] + 1)
answer = []
for s in sources:
    if s == destination:
        answer.append(0)
    elif li[s] >= 999999:
        answer.append(-1)
    else:
        answer.append(li[s])
