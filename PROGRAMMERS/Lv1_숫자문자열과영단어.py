def solution(s):
    d = {'zero': '0', 'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}
    while(True):
        for num in d:
            if num in s:
                s = s.replace(num, d[num])
        if s.isdigit():
            break
    return int(s)
