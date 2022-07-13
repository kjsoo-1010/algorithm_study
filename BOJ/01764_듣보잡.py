n, m = map(int, input().split())
listen = set()
both = []
for _ in range(n):
    listen.add(input())

for _ in range(m):
    see = input()
    if see in listen:
        both.append(see)
both.sort()
print(len(both))
for item in both:
    print(item)
