import sys

input = sys.stdin.readline

for _ in range(int(input())):
    r, strings = input().split()
    for s in strings:
        print(s * int(r), end = '')
    print()
    
