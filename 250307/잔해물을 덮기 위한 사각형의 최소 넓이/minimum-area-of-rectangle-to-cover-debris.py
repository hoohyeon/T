x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())
offset = 1000

points = [[0] * 2000 for _ in range(2000)]

for i in range(x1 + offset, x2 + offset):
    for j in range(y1 + offset, y2 + offset):
        points[i][j] = 1

for i in range(x3 + offset, x4 + offset):
    for j in range(y3 + offset, y4 + offset):
        points[i][j] = 0

min_x, max_x = x2 + offset, x1 + offset
min_y, max_y = y2 + offset, y1 + offset

for i in range(x1 + offset, x2 + offset):
    for j in range(y1 + offset, y2 + offset):
        if points[i][j] == 1:
            min_x = min(min_x, j)
            max_x = max(max_x, j)
            min_y = min(min_y, i)
            max_y = max(max_y, i)

print((max_x - min_x + 1) * (max_y - min_y + 1))