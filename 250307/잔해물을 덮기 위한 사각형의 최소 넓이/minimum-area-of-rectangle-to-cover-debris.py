x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())
offset = 1000

points = [[0] * 2000 for _ in range(2000)]

# 첫 번째 사각형을 1로 설정
for i in range(x1 + offset, x2 + offset):
    for j in range(y1 + offset, y2 + offset):
        points[i][j] = 1

# 두 번째 사각형을 0으로 덮음
for i in range(x3 + offset, x4 + offset):
    for j in range(y3 + offset, y4 + offset):
        points[i][j] = 0

# 최소/최대 x, y 좌표 찾기
min_x, max_x = 2000, -2000
min_y, max_y = 2000, -2000

for i in range(x1 + offset, x2 + offset):
    for j in range(y1 + offset, y2 + offset):
        if points[i][j] == 1:
            min_x = min(min_x, i)
            max_x = max(max_x, i)
            min_y = min(min_y, j)
            max_y = max(max_y, j)

# 사각형이 완전히 지워졌다면 0 출력
if min_x == float('inf'):
    print(0)
else:
    print((max_x - min_x + 1) * (max_y - min_y + 1))
