import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())

M = [ [0] * m for _ in range(n) ]
visited = [ [False] * m for _ in range(n) ]

for _ in range(k):
    t_x, t_y = map(int, input().split())
    M[t_x-1][t_y-1] = 1

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

answer = []

def find(x, y):
    cnt = 1 # 그림 넓이
    q = [(x, y)]
    
    while(True):
        x, y = q.pop(0)

        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]

            if (0<=xx<n and 0<=yy<m):
                if (visited[xx][yy] == False) and (M[xx][yy] == 1):
                    cnt += 1
                    # print(f"{xx}, {yy}")
                    visited[xx][yy] = True
                    q.append((xx, yy))

        if len(q) == 0:
            break
    return cnt
                
    

for i in range(n):
    for j in range(m):
        if M[i][j] == 1 and visited[i][j] == False:
            visited[i][j] = True
            pic = find(i, j)
            answer.append(pic)


if len(answer) == 0:
    print(0)
else:
    print(max(answer))
