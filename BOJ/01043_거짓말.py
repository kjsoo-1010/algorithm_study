import sys

input = sys.stdin.readline

n, m = map(int, input().split())

trues = set(input().split()[1:])

parties = [0] * m
answer = 0

if len(trues) == 0:
    print(m)
    
else:
    for i in range(m):
        party = set(input().split()[1:])
        parties[i] = party
        
    while(True):
        cnt = 0
        for party in parties:
            if (party & trues) and (len(party & trues) != len(party)):
                trues = party | trues
                cnt += 1

        if cnt == 0:
            break

    for party in parties:
        if len(party & trues) == 0:
            answer += 1

    print(answer)
