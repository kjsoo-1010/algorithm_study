n = int(input())
for i in range(-n+1, n) :
  for j in range(-n, n) :
    if (i >= j+1) and (i <=-j-1) :
      print("*", end = '')
    elif (i<=j) and (i>=-j) :
      print("*", end = '')
    else :
      print(" ", end = '')
  print()
