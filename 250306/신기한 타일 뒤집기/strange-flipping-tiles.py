n = int(input())
commands = [tuple(input().split()) for _ in range(n)]
x = []
dir = []
for num, direction in commands:
    x.append(int(num))
    dir.append(direction)

tiles = [[0] for _ in range(2 * 1000 * 100 + 1)]

cur = 100000
for i in range(n):

    if dir[i] == 'R':   # 오른쪽
        for j in range(cur, cur + x[i]):
            tiles[j][0] = 1
        cur = cur + x[i] - 1

    else:   # 왼쪽
        for j in range(cur, cur - x[i], -1):
            tiles[j][0] = -1
        cur = cur - x[i] + 1

w, b = 0, 0

for tile in tiles:
    if tile[0] == -1:
        w += 1
    
    if tile[0] == 1:
        b += 1

    
print(w, b)