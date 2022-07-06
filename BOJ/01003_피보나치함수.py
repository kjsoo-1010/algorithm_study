import sys

input = sys.stdin.readline

def FiboList(num):
  sList = [0, 1, 1]
  for i in range(3, num+2):
    sList.append(sList[i-1] + sList[i-2])
  return sList


for _ in range(int(input())):
    num = int(input())
    if num == 0:
        print(1, 0)
    else:
        li = FiboList(num)
        print(li[num-1], li[num])
