n, t = map(int, input().split())
arr = list(map(int, input().split()))

max_value = 0
cnt = 0

for i in range(n):
    if arr[i] > t:
        cnt += 1

    else:
        cnt = 0

    max_value = max(max_value, cnt)

print(max_value)