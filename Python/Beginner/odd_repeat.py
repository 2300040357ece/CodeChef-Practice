T = int(input())

for _ in range(T):
    N, K, S = map(int, input().split())

    answer = (S - N * N) // (K - 1)

    print(answer)