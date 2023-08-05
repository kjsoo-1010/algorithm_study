import sys

input = sys.stdin.readline

n = int(input())

def find_parent(a):
    if parent[a] != a:
        parent[a] = find_parent(parent[a])
    return parent[a]


def union(a, b):
    a, b = find_parent(a), find_parent(b)

    if a != b:
        parent[b] = a
        f_num[a] += f_num[b] 
        
for _ in range(n):
    
    f = int(input())
    parent = dict()
    f_num = dict()

    for _ in range(f):
        a, b = input().split()

        if a not in parent:
            parent[a] = a
            f_num[a] = 1

        if b not in parent:
            parent[b] = b
            f_num[b] = 1

        union(a, b)

        print(f_num[find_parent(a)])

