import sys

input = sys.stdin.readline

deque = []
for _ in range(int(input())):
    command = input().split()

    if len(deque) == 0 and command[0] in ['pop_front', 'pop_back', 'front', 'back']:
        print(-1)
    else:
        if command[0] == 'push_front':
            deque.insert(0, command[1])
        elif command[0] == 'push_back':
            deque.append(command[1])

        elif command[0] == 'pop_front':
            p = deque.pop(0)
            print(p)
        elif command[0] == 'pop_back':
            p = deque.pop()
            print(p)

        elif command[0] == 'size':
            print(len(deque))

        elif command[0] == 'empty':
            if len(deque) == 0:
                print(1)
            else:
                print(0)
            
        elif command[0] == 'front':
            print(deque[0])
                
        elif command[0] == 'back':
            print(deque[-1])


