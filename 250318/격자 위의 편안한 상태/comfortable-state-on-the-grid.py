n, m = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(m)]
a = [[0] * (n+1) for _ in range(n+1)]

for point in points:
    x, y = point
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
    cnt = 0

    a[x][y] = 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx <= n and 0 <= ny <= n and a[nx][ny] == 1:
            cnt += 1

    if cnt == 3:
        print(1)
    else:
        print(0)
