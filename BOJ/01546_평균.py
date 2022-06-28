n = int(input())
scores = list(map(int, input().split()))
M = max(scores)

avg = (sum(scores)) * 100 / M / n
print(avg)
