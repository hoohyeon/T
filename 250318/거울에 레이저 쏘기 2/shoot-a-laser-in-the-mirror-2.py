n = int(input())
mirror = [list(input()) for _ in range(n)]
k = int(input())

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

dir = (k-1) // n
cnt = 0

start_pos = [(1, k), (k-n, n), (n, 3*n-k+1), (4*n-k+1, 1)]
x, y = start_pos[dir]

mirror_change = {
    '/': {0: 1, 1: 0, 2: 3, 3: 2},
    '\\': {0: 3, 1: 2, 2: 1, 3: 0}
}

while 0 < x <= n and 0 < y <= n:
    if mirror[x-1][y-1] in mirror_change:
        dir = mirror_change[mirror[x-1][y-1]][dir]
    
    x += dx[dir]
    y += dy[dir]
    
    cnt += 1
print(cnt)