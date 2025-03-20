n, s = map(int, input().split())

numbers = list(map(int, input().split()))
min_gap = s

for i in range(n-1):
    for j in range(i+1, n):
        c_sum = sum(numbers) - numbers[i] - numbers[j]
        gap = abs(s - c_sum)

        min_gap = min(min_gap, gap)

print(min_gap)