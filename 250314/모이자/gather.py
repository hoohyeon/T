n = int(input())
A = list(map(int, input().split()))

min_d = int(1e9)

for i in range(n):
    sum_d = 0
    for j in range(n):
        sum_d += abs(i-j) * A[j]
    min_d = min(min_d, sum_d)

print(min_d)