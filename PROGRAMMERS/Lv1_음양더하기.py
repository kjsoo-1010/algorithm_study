def solution(absolutes, signs):
    answer = 0
    n = len(signs)
    for i in range(n):
        if signs[i]:
            answer += absolutes[i]
        else:
            answer += ((-1) * absolutes[i])
    return answer
