def solution(X, Y):
    dic_x, dic_y = {}, {}
    
    x = set(str(X))
    y = set(str(Y))

    for xx in str(X):
        if xx in dic_x:
            dic_x[xx] += 1
        else:
            dic_x[xx] = 1

    for yy in str(Y):
        if yy in dic_y:
            dic_y[yy] += 1
        else:
            dic_y[yy] = 1

    common = x & y
    if common == {'0'}:
        return "0"
    # print(common)
    li = []
    if len(common) == 0:
        return ("-1")
    for elem in common:
    #    print(elem)
    #    print(dic_x)
        m = dic_x[elem]
        if m > dic_y[elem]:
            m = dic_y[elem]
    #    print(m)
        for _ in range(m):
            li.append(elem)
    li.sort(reverse = True)
    answer = ''
    # print(li)
    for l in li:
       answer += l
    return answer
