num = input()
if len(num) == 3:
    if num[1] == '0':
        n = int(num[:2])
        k = int(num[2:])
    else:
        n = int(num[1:])
        k = int(num[:1])
elif len(num)<3:
    n = int(num[0])
    k = int(num[1])
else:
    n, k = 10, 10
print(n+k)
