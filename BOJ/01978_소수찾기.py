import math
cnt = 0
n = int(input())
nums = input().split(" ")
#print(n, nums)
for i in nums :
  if i == '1' :
    cnt +=1
  else :
    i = int(i)
    for j in range(2, int(math.sqrt(i)+1)) :
      if i % j == 0 :
        #print(i, j)
        cnt += 1
        break
print(len(nums)-cnt)
