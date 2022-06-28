while(True):
    li = list(map(int, input().split()))
    if li[0] == 0:
        break
    M = max(li)
    li.remove(M)
    if (li[0] * li[0] + li[1] * li[1]) == M*M:
        print('right')
    else:
        print("wrong")
    
