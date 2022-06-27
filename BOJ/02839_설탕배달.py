n = int(input())
five = n//5
for i in range(five, -1, -1):
    if (n-5*i)%3 == 0:
        print(i+(n-5*i)//3)
        break
    elif i == 0:
        print(-1)
    else:
        continue
