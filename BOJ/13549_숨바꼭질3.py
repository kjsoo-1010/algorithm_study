n, k = map(int, input().split())
MAX = 100000
q = [n]
visited = [-1] * (MAX+1)
visited[n] = 0

while(True):
    x = q.pop(0)

    if x == k:
        #print(f"answer: {visited[x]}")
        print(visited[x])
        break

    # 순간이동 우선
    xx = x*2
    if 0<=xx<=MAX and visited[xx] == -1:
        visited[xx] = visited[x] + 0
        q.append(xx)

    # x-1, x+1
    for xx in (x-1, x+1):
        if 0<=xx<=MAX and visited[xx] == -1:
            visited[xx] = visited[x] + 1
            q.append(xx)

    #print(q)
    #for qq in q:
    #    print(visited[qq], end = ' ')
    #input()
