n = int(input())
if n % 2 == 0 :
  for i in range(1, 2*n+1) :
    if i %2 != 0 :
        print("* " * (n//2-1)+"*")
    else :
        print(" *"*(n//2))
else :
  for i in range(1, 2*n +1) :
    if i%2== 0 :
        print(" *" * (n//2))
    else :
        print("* " * (n//2) + "*")
