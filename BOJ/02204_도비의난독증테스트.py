while True :
    n = int(input())
    dic = {}
    if n == 0:
        break
    for i in range(0, n) :
        s = input()
        dic[s.upper()] = s
    dic = sorted(dic.items())
    print(dic[0][1])
