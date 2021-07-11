n = int(input())
for i in range(0, 2*n) :
  if i < n :
    print((" " * i) + ("*" * ((2*(n-i))-1)))
  elif i == n :
    pass
  else :
    i = i-n+1
    print((" " * (n-i)) + ("*" * (2*i-1)))
