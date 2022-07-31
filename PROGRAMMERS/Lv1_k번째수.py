def solution(array, commands):
    answer = []
    for com in commands:
        top = com[0]
        mid = com[1]
        bot = com[2]
        arr = array[top-1:mid]
        arr.sort()
        k = arr[bot-1]
        answer.append(k)
    return answer
