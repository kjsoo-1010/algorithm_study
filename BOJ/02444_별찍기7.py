n = int(input())
for i in range(1, 2*n +1) :
  if (i <=n) :
    print((" " * (n-i)) + ("*"*(2*i-1)))
  else :
    i -= n
    print((" "*(i)) + ("*"*(2*(n-i-1)+1)))
