n = input()
for i in range(0, int(n)) :
    print(("%" + n + "s") %("*"*(int(n)-i)))
