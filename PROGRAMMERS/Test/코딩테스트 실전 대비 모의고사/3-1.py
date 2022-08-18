def solution(a, b, n):
    answer = 0
    while (True):
        answer += (n // a) * b
        if n // a == 0:
            break
        n = b * (n // a) + n % a
        
    return answer

print(solution(5, 2, 20))
