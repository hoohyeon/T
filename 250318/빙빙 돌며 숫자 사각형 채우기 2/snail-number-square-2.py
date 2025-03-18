n, m = map(int, input().split())

arr = [[0] * m for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
x, y = 0, 0
dir = 0
number = 2

arr[x][y] = 1

for number in range(2, n * m + 1):
    nx = x + dx[dir]
    ny = y + dy[dir]

    if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 0:
        x, y = nx, ny

    else:
        dir = (dir + 1) % 4
        x, y = x + dx[dir], y + dy[dir]
    
    arr[x][y] = number

for row in arr:
    print(*row)
