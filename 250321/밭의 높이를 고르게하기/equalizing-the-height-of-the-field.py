n, h, t = map(int, input().split())

field = list(map(int, input().split()))
new_field = [0] * 6

for i in range(n):
    new_field[i] = abs(h - field[i])

min_cost = sum(new_field)

for i in range(n-t+1):
    cost = sum(new_field[i:i+t])
    min_cost = min(min_cost, cost)

print(min_cost)