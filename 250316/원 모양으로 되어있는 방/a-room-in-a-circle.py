n = int(input())
a = [int(input()) for _ in range(n)]

min_d = int(1e9)

for i in range(n):  # i index 시작
    sum_d = 0

    for j in range(n):  # j index 도착
        if i <= j:
            sum_d += (j - i) * a[j]

        else:
            sum_d += (n - i + j) * a[j]

    min_d = min(min_d, sum_d)

print(min_d)