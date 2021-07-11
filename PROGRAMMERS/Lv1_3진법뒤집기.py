def solution(n):
    answer = ""
    while (True) :
        new = str(n % 3)
        answer += new
        n = n//3
        if n == 0 :
            break
    answer = int(answer)
    answer = str(answer)
    return (int(answer, 3))
