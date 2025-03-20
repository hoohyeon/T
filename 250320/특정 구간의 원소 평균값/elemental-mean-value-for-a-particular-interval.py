n = int(input())
nums = list(map(int, input().split()))

cnt = 0
for i in range(n):
    for j in range(i, n):
        interval = nums[i:j+1]

        avg = sum(interval) / len(interval)

        if avg in interval:
            cnt += 1

print(cnt)