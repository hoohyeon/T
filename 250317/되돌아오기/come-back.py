n = int(input())
moves = [tuple(input().split()) for _ in range(n)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]

direction_dict = {'W' : (-1, 0), 'S' : (0, -1), 'N' : (0, 1), 'E' : (1, 0)}

x, y = 0, 0
time = 0
result = -1
check = False

for i in range(n):
    dx, dy = direction_dict[dir[i]]

    for _ in range(dist[i]):

        x += dx
        y += dy
        time += 1

        if x == 0 and y == 0 and not check:
            result = time
            check = True
            break

print(result)