'''
import re

str = "Hello, World, Python"
result = re.sub(",", "", str)
print(result)
'''

def solution(ingredient):
    s = ''.join(map(str, ingredient))
    answer = 0
    # print(s)
    while('1231' in s):
        print(s)
        s = s.replace('1231', '')
        answer += 1
    return answer

print(solution([2, 1, 1, 2, 3, 1, 2, 3, 1]))
