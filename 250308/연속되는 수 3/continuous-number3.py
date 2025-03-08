n = int(input())
arr = [int(input()) for _ in range(n)]

max_value = 0
cnt = 1

for i in range(1, n):
    if arr[i-1] * arr[i] > 0:
        cnt += 1
    else:
        cnt = 1

    max_value = max(max_value, cnt)

print(max_value)