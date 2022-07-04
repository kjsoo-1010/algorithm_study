import sys

input = sys.stdin.readline

for _ in range(int(input())):
    cnt = 0
    n, m = map(int, input().split())
    li = list(map(int, input().split()))
    M = max(li)
    
    p = li[m]
    
    q = [(i, li[i]) for i in range(n)]
    
    while(True):        
        last = q.pop(0)
        if last[1] != M:
            q.append(last)
        else:
            cnt += 1
            li.remove(last[1])
            
            if last == (m, p):
                print(cnt)
                break
            
            M = max(li)
