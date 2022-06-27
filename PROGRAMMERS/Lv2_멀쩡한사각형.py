def solution(w,h):
    ### 최대공약수 구해서 나눠서 작은 직사각형 만들기
    # w, h 중 큰 값이 b, 작은 값을 a
    # (b/a 몫 +1)만큼 b에서 빼고 a 곱하기 = 넓이
    if w > h :
        b=w
        a=h
    else :
        b=h
        a=w
    from math import gcd
    if gcd(a,b) == 1 :
        answer = a*b-(a+b-1)
    else :
        answer = a*b-(a+b-gcd(a,b))
    return answer
