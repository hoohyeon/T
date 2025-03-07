n = int(input())
x1, y1, x2, y2 = [], [], [], []

for _ in range(n):
    a, b, c, d = map(int, input().split())
    x1.append(a)
    y1.append(b)
    x2.append(c)
    y2.append(d)

points = [[0] * 200 for _ in range(200)]
offset = 100

for i in range(n):
    for j in range(x1[i] + offset, x2[i] + offset):
        for k in range(y1[i] + offset, y2[i] + offset):
            points[j][k] = 1

total = 0
for row in points:
    total += sum(row)

print(total)