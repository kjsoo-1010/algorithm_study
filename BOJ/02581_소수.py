import math
M = int(input())
N = int(input())
odd = []
odd_check = True
for i in range(M, N+1) :
  if i == 1 :
    odd_check = False
  elif i == 2 :
    odd_check = True
  else :
    for j in range(2, int(math.sqrt(i)+1)) :
      odd_check = True
      if i % j == 0 :
        odd_check = False
        break
  if odd_check == True :
    odd.append(i)
if len(odd) == 0 :
  print(-1)
else :
  #print(odd)
  print(sum(odd))
  print(odd[0])
