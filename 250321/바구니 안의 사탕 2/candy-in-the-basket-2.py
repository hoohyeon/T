n, k = map(int, input().split())

basket = [0] * 101

for _ in range(n):
    candy, coor = map(int, input().split())

    basket[coor] += candy

max_sum = 0
for c in range(1, 100 + 1):
    c_sum = sum(basket[c-k:c+k+1])

    max_sum = max(max_sum, c_sum)

print(max_sum)