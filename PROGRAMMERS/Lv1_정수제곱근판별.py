def solution(n):
    sqt = n**(1/2)
    # print(sqt)
    if sqt == int(sqt):
        return ((int(sqt)+1)**2)
    else:
        return -1
