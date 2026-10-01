T = int(input())

for _ in range(T):
    D = input().strip()

    if D.count('0') == 1 or D.count('1') == 1:
        print("Yes")
    else:
        print("No")