n = int(input())
commands = [tuple(input().split()) for _ in range(n)]
x = []
dir = []
for num, direction in commands:
    x.append(int(num))
    dir.append(direction)

tiles = [[0, 0, -1] for _ in range(2 * n * 100 + 1)] # [0] = 흰색, [1] = 검은색, [2] = 마지막 색

cur = 100
for i in range(n):

    if dir[i] == 'R':   # 오른쪽
        for j in range(cur, cur + x[i]):
            tiles[j][1] += 1
            tiles[j][2] = 1
        cur = cur + x[i] - 1

    else:   # 왼쪽
        for j in range(cur, cur - x[i], -1):
            tiles[j][0] += 1
            tiles[j][2] = 0
        cur = cur - x[i] + 1

w, b, g = 0, 0, 0

for tile in tiles:
    if tile[0] >= 2 and tile[1] >= 2:
        g += 1

    elif tile[0] > tile[1]:
        w += 1

    elif tile[0] < tile[1]:
        b += 1

    else:
        if tile[2] == 0:
            w += 1
        elif tile[2] == 1:
            b += 1

print(w, b, g)