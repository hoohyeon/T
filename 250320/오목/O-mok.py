board = [list(map(int, input().split())) for _ in range(19)]

def f(board):
    dx = [0, 1, 1, -1]
    dy = [1, 0, 1, 1]

    for x in range(19):
        for y in range(19):
            if board[x][y] == 0:
                continue

            stone = board[x][y]
            for dir in range(4):
                streak = 1
                for n in range(1, 5):
                    nx = x + dx[dir] * n
                    ny = y + dy[dir] * n

                    if not (0 <= nx < 19 and 0 <= ny < 19):
                        break

                    if board[nx][ny] == stone:
                        streak += 1
                    else:
                        break

                if streak == 5:
                    mid_x = x + dx[dir] * 2
                    mid_y = y + dy[dir] * 2
                    return stone, mid_x + 1, mid_y + 1
        
    return 0

result = f(board)

if result == 0:
    print(0)

else:
    print(result[0])
    print(result[1], result[2])

