n = int(input())
for i in range(1, n+1) :
  if i == 1 :
    print((" " * (n-i)) + "*")
  else :
    print((" " * (n-i))+"*" + (" "*(2*(i-1)-1)) + "*")
