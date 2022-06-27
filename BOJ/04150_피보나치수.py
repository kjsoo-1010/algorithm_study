import sys
sys.getrecursionlimit(10**6)

def fibo(arr, count, n):
    arr.append(arr[count-1] + arr[count-2])
    if count == n:
        return arr[n]
    fibo(arr, count+1, n)
    return arr[n]

n = int(input())
arr = [0, 1, 1]

if n == 0:
    print(arr[0])
elif n == 1:
    print(arr[1])
elif n == 2:
    print(arr[2])
else :
    print(fibo(arr, 3, n))
