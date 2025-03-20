n, m = map(int, input().split())

board = [list(input()) for _ in range(n)]

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0 , 1, -1, 1, -1, 0, 1]

cnt = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == 'L':
            x, y = i, j
            for dir in range(8):
                nx1, ny1 = x + dx[dir], y + dy[dir]
                nx2, ny2 = nx1 + dx[dir], ny1 + dy[dir]

                valid_1 = 0 <= nx1 < n and 0 <= ny1 < m and board[nx1][ny1] == 'E'
                valid_2 = 0 <= nx2 < n and 0 <= ny2 < m and board[nx2][ny2] == 'E'
                if valid_1 and valid_2:
                    cnt += 1

print(cnt)