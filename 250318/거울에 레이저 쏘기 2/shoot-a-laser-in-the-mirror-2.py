n = int(input())
mirror = [list(input()) for _ in range(n)]
k = int(input())
razer = [[0] * (n+1) for _ in range(n+1)]

dir = (k-1) // n
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
cnt = 0

if dir == 0:
    x, y = (1, k)
elif dir == 1:
    x, y = (k-n, n)
elif dir == 2:
    x, y = (n, 3*n-k+1)
elif dir == 3:
    x, y = (4*n-k+1, 1)

while 0 < x < n and 0 < y < n:
    if mirror[x-1][y-1] == '/':
        if dir == 0:
            dir = 1
        elif dir == 1:
            dir = 0
        elif dir == 2:
            dir = 3
        elif dir == 3:
            dir = 2

    elif mirror[x-1][y-1] == '\\':
        if dir == 0:
            dir = 3
        elif dir == 1:
            dir = 2
        elif dir == 2:
            dir = 1
        elif dir == 3:
            dir = 0

    x += dx[dir]
    y += dy[dir]
    
    cnt += 1

print(cnt)