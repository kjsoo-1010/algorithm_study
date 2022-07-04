import sys

input = sys.stdin.readline
n = int(input())

dic = {}
li = []


for _ in range(n):
    tmp = int(input())
    li.append(tmp)
    if tmp in dic:
        dic[tmp] += 1
    else:
        dic[tmp] = 1
li.sort()

print(round(sum(li)/n))# 1. 산술평균
print(li[n//2]) # 2. 중앙값

cnt = [k for k, v in dic.items() if v == max(dic.values())]
cnt.sort()

if len(cnt) == 1:
    print(cnt[0])
else:
    print(cnt[1]) # 3. 최빈값

print(max(li) - min(li)) # 4. 범위
