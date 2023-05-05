a, b, c = map(int, input().split())
i = 1
while True:
    if i % a == 0:
        if i % b == 0:
            if i % c == 0:
                break
    i += 1
print(i)
