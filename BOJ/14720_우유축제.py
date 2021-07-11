n = int(input())
nums = input().split(" ")
cnt = 0
start = 0
now = '0'
for i in range(0, len(nums)) :
  if nums[i] == '0' :
    start = i
    cnt += 1
    break
for i in range(start, len(nums)) :
  if now == '0' and nums[i] == '1' :
    cnt += 1
    now = '1'
  elif now == '1' and nums[i] == '2' :
    cnt += 1
    now = '2'
  elif now == '2' and nums[i] == '0' :
    cnt += 1
    now = '0'
  else :
    pass

print(cnt)
