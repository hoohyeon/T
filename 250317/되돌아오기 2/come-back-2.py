commands = input()

x, y = 0, 0
dir = 0
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
time = 0
ans = -1

for command in commands:
    if command == 'L':
        dir = (dir - 1 + 4) % 4 
    elif command == 'R':
        dir = (dir + 1 + 4) % 4     
    else:
        x += dx[dir]
        y += dy[dir]
    
    time += 1

    if x == 0 and y == 0 and ans == -1:
        ans = time
        break

print(ans)