n, k = map(int, input().split())

nums = list(map(int, input().split()))
max_sum = 0

for i in range(n-k+1):
    c_sum = sum(nums[i:i+k])

    max_sum = max(max_sum, c_sum)

print(max_sum)