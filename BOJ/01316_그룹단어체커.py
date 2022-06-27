n = int(input())
no_group = 0
for i in range(0, n):
    word = input()
    word_list = list(set(word))
    for w in word_list:
        cnt = word.count(w)
        if cnt != 1:
            index = word.find(w)
            if word[index:index+cnt] != w*cnt:
                no_group +=1
                break
print(n-no_group)
