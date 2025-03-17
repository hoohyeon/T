N = int(input())
moves = [tuple(input().split()) for _ in range(N)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]

direction_map = {'N': (0, 1), 'S': (0, -1), 'E': (1, 0), 'W': (-1, 0)}

x, y = 0, 0
time = 0
result = - 1

for i in range(N):
    dx, dy = direction_map[dir[i]]

    for _ in range(dist[i]):
        x += dx
        y += dy
        time += 1

        if x == 0 and y == 0:
            result = time
            break

print(result)