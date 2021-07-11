n = int(input())
for i in range(1, 2*n) :
  if i <= n :
    print("*"*i)
  else :
    i -= n
    print("*"*(n-i))
