string = input().upper()


setString = set(string)
dic = {}

for item in setString:
    dic[item] = string.count(item)

li = [key for key, value in dic.items() if max(dic.values()) == value]

if len(li) > 1:
    print('?')
else:
    print(li[0])
