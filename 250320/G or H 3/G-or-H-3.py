n, k = map(int, input().split())
arr = [0] * 10001
max_sum = 0

for _ in range(n):
    p, a = input().split()
    p = int(p)

    if a == 'G':
        arr[p] = 1
    
    elif a == 'H':
        arr[p] = 2

for i in range(10001-k):
    c_sum = sum(arr[i:i+k+1])
    max_sum = max(max_sum, c_sum)

print(max_sum)