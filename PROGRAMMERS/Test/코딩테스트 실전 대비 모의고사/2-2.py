def solution(topping):
    answer = 0
    for i in range(len(topping)):
        first = set(topping[i:])
        second = set(topping[:i])
        if len(first) == len(second):
            answer += 1
    return answer
