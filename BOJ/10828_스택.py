import sys

input = sys.stdin.readline

stack = []
for _ in range(int(input())):
    command = input().split()

    if command[0] == 'push':
        stack.append(command[1])
    elif command[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
    elif command[0] == 'size':
        print(len(stack))
    elif command[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            p = stack.pop()
            print(p)
    elif command[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
