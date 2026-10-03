t = int(input())

for _ in range(t):
    a, b, p, q = map(int, input().split())

    if a == p and b == q:
        print(0)

    elif (a + b) % 2 != (p + q) % 2:
        print(1)

    else:
        print(2)