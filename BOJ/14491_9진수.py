n = int(input())
answer = ""
while (True) :
  new = "%d" %(n % 9)
  answer = new + answer
  n = n//9
  if n  == 0 :
    break

print(int(answer))
