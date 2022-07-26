import math

n = int(input())

if n == 1:
    x = 1
elif n < 3 :
    x = 2
else:
    # 3n^2 - 9n + (7-n) = 0

    a = 3
    b = -9
    c = (7-n)

    x = (-b + (b**2-4*a*c)**0.5)/(2*a)
print(int(x))
