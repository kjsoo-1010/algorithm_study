def solution(n, lost, reserve):
    cnt = 0
    for item in lost:
        if item + 1 in reserve:
            cnt += 1
            reserve.remove(item+1)
        elif item - 1 in reserve:
            cnt += 1
            reserve.remove(item-1)
    answer = n - len(lost) + cnt
    return answer
