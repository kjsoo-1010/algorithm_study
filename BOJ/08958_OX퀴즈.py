for _ in range(int(input())):
    o = input().split('X')
    total = 0
    # print(o)
    for i in o:
        n = len(i)
        total += (1+n) * n / 2
    print(int(total))
