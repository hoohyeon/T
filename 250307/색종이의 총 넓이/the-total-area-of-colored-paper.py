n = int(input())
point = [tuple(map(int, input().split())) for _ in range(n)]

offset = 100

points = [[0] * 200 for _ in range(200)]

for p in point:
    for x in range(p[0] + offset, p[0] + offset + 8):
        for y in range(p[1] + offset, p[1] + offset + 8):
            points[x][y] = 1

area = 0

for row in points:
    area += sum(row)

print(area)