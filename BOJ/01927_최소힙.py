import sys
import heapq

input = sys.stdin.readline
print = sys.stdout.write

h = []
    
for _ in range(int(input())):
    
    command = int(input())

    if len(h) == 0 and command == 0:
        print('0\n')
    elif command == 0:
        m = heapq.heappop(h)
        print(f'{m}\n')
    else:
        heapq.heappush(h, command)
    # print(f'{command}\n')
