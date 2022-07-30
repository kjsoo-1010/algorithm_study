def solution(lottos, win_nums):
    zero = lottos.count(0)
    lottos = set(lottos)
    win_nums = set(win_nums)
    common = lottos & win_nums
    
    if len(common) < 2:
        n = 6
    elif len(common) > 5:
        n = 1
    else:
        n = 7 - len(common)
    
    if len(common) + zero < 2:
        nn = 6
    elif len(common) + zero > 5:
        nn = 1
    else:
        nn = 7 - (len(common) + zero)
    
    answer = [nn, n]
    
    return answer
