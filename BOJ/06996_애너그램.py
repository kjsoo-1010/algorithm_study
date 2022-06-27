n = int(input())
for i in range(0, n) :
  li = input().split(" ")
  #s2 = input()
  if sorted(li[0]) == sorted(li[1]):
    print(f"{li[0]} & {li[1]} are anagrams.")
  else :
    print(f"{li[0]} & {li[1]} are NOT anagrams.")
