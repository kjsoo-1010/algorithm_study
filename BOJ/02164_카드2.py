n = int(input())
binNum = bin(n)[2:]
binary = len(binNum)
if binNum.count('1') == 1:
    print(n)
else:
    print((n - 2**(binary-1))*2)
