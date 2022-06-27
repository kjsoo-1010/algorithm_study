n = int(input())
nums = list(map(int, input().split(' ')))
acc = [nums[0]]
sum = sum(nums)
for i in range(1, n):
    acc.append(acc[-1]+nums[i])
answer = 0
for i in range(0, n-1):
    #print(nums[i], acc[i+1], sum-acc[i])
    answer += nums[i]*(sum-acc[i])
print(answer)
