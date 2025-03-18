n = int(input())

arr = [[0] * n for _ in range(n)]

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]
dir = 0

x, y = n-1, n-1
start = n * n
arr[x][y] = start

for number in range(start-1, 0, -1):
    nx = x + dx[dir]
    ny = y + dy[dir]

    if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == 0:
        x = nx
        y = ny

    else:
        dir = (dir + 1) % 4
        x, y = x + dx[dir], y + dy[dir]

    arr[x][y] = number

for row in arr:
    print(*row)
