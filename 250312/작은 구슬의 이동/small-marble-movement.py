n, t = map(int, input().split())
r, c, d = input().split()
r, c = int(r), int(c)

dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
direct = {'U': 0, 'R': 1, 'D': 2, 'L': 3 }
dir_num = direct[d]

time = 0
while time < t:
    r += dx[dir_num]
    c += dy[dir_num]

    if not (0 < r <= n and 0 < c <= n):
        r -= dx[dir_num]
        c -= dy[dir_num]

        dir_num = (dir_num + 2) % 4

    time += 1
print(r, c)