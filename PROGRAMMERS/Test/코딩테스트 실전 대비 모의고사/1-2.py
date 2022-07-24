def solution(w, n, dis):
    dic = {}
    for i in range(len(w)):
        dic[w[i]] = n[i]
    
    cnt = 0
    for i in range(len(dis) - 9):
        li = dis[i:i+10]
        if set(li) != set(w):
            pass
        else:
            p = 0
            for ww in w:
                if li.count(ww) == dic[ww]:
                    p += 1
                else:
                    pass
            if p == len(n):
                print(i)
                cnt += 1
            print(cnt)

    return int(cnt)
