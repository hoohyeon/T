n = int(input())

x, y = 0, 0
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]

for _ in range(n):
    dir, d = input().split()
    d = int(d)

    if dir == 'W':
        x, y = x + d * dx[2], y + d * dy[2]
    
    elif dir == 'S':
        x, y = x + d * dx[1], y + d * dy[1]

    elif dir == 'N':
        x, y = x + d * dx[3], y + d * dy[3]

    else:
        x, y = x + d * dx[0], y + d * dy[0]

print(x, y)