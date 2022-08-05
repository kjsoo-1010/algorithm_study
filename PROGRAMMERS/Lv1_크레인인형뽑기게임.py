def solution(board, moves):
    n = len(board)
    li = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if board[j][i] != 0:
                li[i].append(board[j][i])
    # print(li)
    stack = []
    answer = 0
    for item in moves:
        item -= 1
        if len(li[item]) > 0:
            p = li[item].pop(0)
            stack.append(p)
            
        if len(stack) > 1 and stack[-1] == stack[-2]:
            stack.pop()
            stack.pop()
            answer += 2
            
    # print(stack)

    return answer
