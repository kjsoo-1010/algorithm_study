for i in range(0, 2) :
  score = []
  for i in range(0, 10) :
      score.append(int(input()))
      score.sort()
  print(sum(score[-3:]))
