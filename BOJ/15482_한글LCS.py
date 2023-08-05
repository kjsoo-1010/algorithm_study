a, b = input(), input()

li = [0] * 1000

for i in range(len(a)):
    M = 0 # 더 큰 값 저장
    for j in range(len(b)):
        if M < li[j]:
            

print(max(li))
