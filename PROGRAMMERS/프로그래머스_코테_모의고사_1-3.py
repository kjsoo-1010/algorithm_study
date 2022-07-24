def solution(order):
    first = order[0]
    sub = [i for i in range(1, first)]
    li = [i for i in range(first+1, len(order)+1)][::-1]
    order = order[1:]
    
    #print(sub)
    #print(li)
    #print(order)

    cnt = 1
    for i in range(0, len(order)):
        item = order[i]
        # print(item)
        if sub and item == sub[-1]:
            sub.pop()
            cnt += 1
        elif li and item == li[-1]:
            li.pop()
            cnt += 1
        else:
            if li and item > li[-1]:
                while(True):
                    sub.append(li.pop())
                    #print(sub)
                    #print(li)
                    if li and li[-1] == item:
                        break
                li.pop()
                #print(li)
                cnt += 1
            else:
                break

    return cnt
