x1 = [0] * 3
y1 = [0] * 3
x2 = [0] * 3
y2 = [0] * 3

x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())
x1[2], y1[2], x2[2], y2[2] = map(int, input().split())

offset = 1000
points = [[0] * 2000 for _ in range(2000)]

for x in range(x1[0] + offset, x2[0] + offset):
    for y in range(y1[0] + offset, y2[0] + offset):
        points[x][y] = 1

for x in range(x1[1] + offset, x2[1] + offset):
    for y in range(y1[1] + offset, y2[1] + offset):
        points[x][y] = 1

for x in range(x1[2] + offset, x2[2] + offset):
    for y in range(y1[2] + offset, y2[2] + offset):
        points[x][y] = 0

area = 0
for row in points:
    area += sum(row)

print(area)
