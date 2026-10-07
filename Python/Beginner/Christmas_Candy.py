T = int(input())

for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))

    max_so_far = A[0]
    count = 0

    for i in range(1, N):
        if A[i] < max_so_far:
            count += 1

        max_so_far = max(max_so_far, A[i])

    print(count)