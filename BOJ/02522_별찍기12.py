n = int(input())
for i in range(1, 2*n) :
  if i <= n:
    print((" " *(n-i))+("*" * i))
  else :
    i -= n
    print((" " * i) + ("*" *(n-i)))
