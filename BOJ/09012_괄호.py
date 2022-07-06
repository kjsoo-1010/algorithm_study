import sys

input = sys.stdin.readline

for _ in range(int(input())):
    string = input().strip()
    tmp = 0
    for i in range(len(string)):
        if string[i] == '(':
            tmp += 1
        elif string[i] == ')':
            tmp -= 1
        else:
            pass

        if tmp < 0:
            print("NO")
            break

        if i == len(string) -1:
            if tmp == 0:
                print("YES")
            else:
                print("NO")
