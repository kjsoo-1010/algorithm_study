def solve(code):
    brackets = []
    for i in code:
        if i not in '()[]{}':
            continue
        elif i in '([{':
            brackets.append(i)
        elif i == ')':
            if brackets[-1] == '(':
                brackets.pop()
            else:
                print("Illegal")
                return 0
            
        elif i == ']':
            if brackets[-1] == '[':
                brackets.pop()
            else:
                print("Illegal")
                return 0

        elif i == '}':
            if brackets[-1] == '{':
                brackets.pop()
            else:
                print("Illegal")
                return 0
    if len(brackets) == 0:
        print("Legal")
    else:
        print("Illegal")
    return


while(True):
    code = input()
    if code == '#':
        break
    else:
        solve(code)
