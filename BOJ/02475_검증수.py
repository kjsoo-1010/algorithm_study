n = list(map(int, input().split()))
total = 0
for item in n:
    total += item*item
print(total%10)
