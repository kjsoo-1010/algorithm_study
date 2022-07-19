import sys

input = sys.stdin.readline

n, m = map(int, input().split())
chess = []
for _ in range(n):
    chess.append(input())

mm = []
for i in range(n-7):
    for j in range(m-7):
        cntB = 0
        cntW = 0
        for k in range(i, i+8):
            for l in range(j, j+8):
                if (k+l) % 2 == 0:
                    if chess[k][l] != 'B':
                        cntB += 1
                    if chess[k][l] != 'W':
                        cntW += 1

                else:
                    if chess[k][l] != 'B':
                        cntW += 1
                    if chess[k][l] != 'W':
                        cntB += 1

        
        mm.append(cntW)
        mm.append(cntB)

print(min(mm))
