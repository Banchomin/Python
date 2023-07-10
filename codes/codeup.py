a = int(input())

b = tuple(map(int, (input().split())))

c = 0
for i in range(len(b)):
    if b[i] > c:
        c = b[i]
