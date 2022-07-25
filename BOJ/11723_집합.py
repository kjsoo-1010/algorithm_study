import sys

input = sys.stdin.readline

s = set()

for _ in range(int(input())):
    command = input().split()
    # print(command)
    if len(command) == 2:
        x = int(command[1])
    
    if command[0] == 'add':
        s.add(x)
    
    elif command[0] == 'remove':
        s.discard(x)
    
    elif command[0] == 'check':
        if x in s:
            print(1)
        else:
            print(0)
    
    elif command[0] == 'toggle':
        if x in s:
            s.remove(x)
        else:
            s.add(x)
    
    elif command[0] == 'all':
        s = set([i for i in range(1, 21)])
    
    elif command[0] == 'empty':
        s = set([])
    
    else:
        pass

    # print(s)
    
