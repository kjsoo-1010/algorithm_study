n, k = map(int, input().split())

q = [n] # 위치 큐
visited = [0] * 200000

while(True):
    x = q.pop(0)

    if x == k:
        print(visited[x])
        break
    for xx in (x-1, x+1, x*2):
        if 0<=xx<=100000 and not visited[xx]:
            visited[xx] = visited[x] + 1
            q.append(xx)
