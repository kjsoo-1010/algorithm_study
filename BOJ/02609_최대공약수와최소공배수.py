import math

a, b = map(int, input().split())
M = math.gcd(a, b)
print(M)
print(a*b//M)
