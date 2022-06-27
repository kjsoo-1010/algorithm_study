def func(arr, count, n):
    arr.append(arr[count-1] + arr[count-2]*2)
    if count == n:
        return arr[n]
    func(arr, count+1, n)
    return arr[n]


n = int(input())
arr = [0, 1, 3]

if n == 0:
    print(arr[0])
elif n == 1:
    print(arr[1])
elif n == 2:
    print(arr[2])
else :
    print(func(arr, 3, n)%10007)
