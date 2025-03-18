n, t = map(int, input().split())
commands = input()
arr = [(list(map(int, input().split()))) for _ in range(n)]

x, y = n // 2, n // 2
result = arr[x][y]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
dir = 0

for command in commands:
    if command == 'L':
        dir = (dir + 1 + 4) % 4
    elif command == 'R':
        dir = (dir - 1 + 4) % 4

    else:
        nx = x + dx[dir]
        ny = y + dy[dir]

        if 0 <= nx < n and 0 <= ny < n:
            x, y = nx, ny
            result += arr[x][y]

print(result)