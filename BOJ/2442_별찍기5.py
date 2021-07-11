n = int(input())
h = n//2
for i in range(0, n) :
    for j in range((-2)*h, 2*h+1) :
        if (-j<=i) and (j<=i):
            print("*", end = '')
        elif (j <= i) :
            print(" ", end = '')
    print()
