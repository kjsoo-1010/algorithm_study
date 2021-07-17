n = int(input())
dic = {}
for i in range(0, n) :
  s = input()
  dic[s] = len(s)

dic_value = sorted(dic.items(), key = lambda item: (item[1], item[0]))

for key, value in dic_value:
  print(key)
