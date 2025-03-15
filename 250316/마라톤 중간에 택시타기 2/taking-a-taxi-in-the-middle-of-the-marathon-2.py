n = int(input())
cp = [tuple(map(int, input().split())) for _ in range(n)]

min_d = int(1e9)

for i in range(1, n-1): # i번째 건너뛰기
    new_d = 0

    prev = 0
    for j in range(1, n):
        if i == j:
            continue

        new_d += abs(cp[j][0] - cp[prev][0]) + abs(cp[j][1] - cp[prev][1])
        prev = j

    min_d = min(min_d, new_d)

print(min_d)