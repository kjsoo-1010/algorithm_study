import math

def k_notation(n, base):
    T = "0123456789"
    q, r = divmod(n, base)
    return k_notation(q, base) + T[r] if q else T[r]

def is_prime(num):
    if num == 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, int(math.sqrt(num))+1):
            if num % i == 0:
                return False
    
    return True


def solution(n, k):
    answer = 0
    notation = k_notation(n, k)
    li = notation.split('0')
    for num in li:
        if len(num) != 0 and is_prime(int(num)):
            answer += 1
            # print(int(num))
    return answer
