n, m = map(int, input().split())

x, y = 0, 0
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
dir = 0
arr = [[0] * m for _ in range(n)]
arr[x][y] = 1

for i in range(2, n * m + 1):
    nx, ny = x + dx[dir], y + dy[dir]

    if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 0:
        x, y = nx, ny

    else:
        dir = (dir + 1) % 4
        x, y = x + dx[dir], y + dy[dir]

    arr[x][y] = i

for row in arr:
    print(*row)