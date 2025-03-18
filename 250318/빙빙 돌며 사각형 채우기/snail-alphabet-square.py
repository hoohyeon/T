n, m = map(int, input().split())

arr = [[''] * m for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

x, y = 0, 0
dir = 0
current_letter = ord('A')  # 'A'부터 시작

arr[x][y] = chr(current_letter)

for _ in range(2, n * m + 1):
    nx = x + dx[dir]
    ny = y + dy[dir]

    if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == '':
        x, y = nx, ny

    else:
        dir = (dir + 1) % 4
        x, y = x + dx[dir], y + dy[dir]
    
    current_letter = ord('A') + (current_letter - ord('A') + 1) % 26  
    arr[x][y] = chr(current_letter)

for row in arr:
    print(*row)
