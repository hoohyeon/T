dirs = input()

dirs_num = 0
x, y = 0, 0
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

for dir in dirs:
    if dir == 'L':
        dirs_num = (dirs_num - 1 + 4) % 4
    elif dir == 'R':
        dirs_num = (dirs_num + 1 + 4) % 4
    else:
        x, y = x + dx[dirs_num], y + dy[dirs_num]

print(x, y)