n = int(input())
numbers = list(map(int, input().split()))

max_sum = 0

for i in range(n):
    for j in range(i+2, n):
        sum = numbers[i] + numbers[j]
        
        max_sum = max(max_sum, sum)

print(max_sum)