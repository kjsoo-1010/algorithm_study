import sys

input = sys.stdin.readline

tmp = input()
li = list(map(int, input().split()))

print(f'{min(li)} {max(li)}')
