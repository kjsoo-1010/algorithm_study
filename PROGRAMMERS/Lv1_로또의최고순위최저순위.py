def solution(lottos, win_nums):
    zero = lottos.count(0)
    lottos = set(lottos)
    win_nums = set(win_nums)
    common = lottos & win_nums
    answer = [7 - len(common) - zero]
    if len(common) == 0:
        answer.append(6)
    else:
        if zero == 0:
            answer = [6 - len(common)]
        answer.append(7-len(common))
    return answer
