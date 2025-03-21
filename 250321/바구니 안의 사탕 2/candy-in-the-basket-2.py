n, k = map(int, input().split())

basket = [0] * 100

for _ in range(n):
    candy, coor = map(int, input().split())

    basket[coor] += candy

max_sum = 0
for c in range(k, (100-k) + 1):
    c_sum = sum(basket[c-k:c+k+1])

    max_sum = max(max_sum, c_sum)

print(max_sum)