a = ''
n = int(input())
N = list(map(int, input().split(' ')))
dic = {}
for item in N:
    try: dic[item] +=1
    except : dic[item] = 1
# print(dic)

m = input()
M = list(map(int, input().split(' ')))

for item in M:
    try:
        a+= ("%d " %dic[int(item)])
    except:
        a += '0 '
print(a.strip())
