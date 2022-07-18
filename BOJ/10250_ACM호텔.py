def solution(h, w, n):

    first = n % h 
    second = n // h + 1

    if first == 0:
        second -= 1
        first = h
    
    if second < 10:
        second = '0' + str(second)
    else:
        second = str(second)

    return str(first) + second
    

for _ in range(int(input())):
    h, w, n = map(int, input().split())
    print(solution(h, w, n))
