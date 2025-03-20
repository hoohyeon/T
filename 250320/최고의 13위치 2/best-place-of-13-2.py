n = int(input())

board = [list(map(int, input().split())) for _ in range(n)]

max_cnt = 0

for i in range(n):
    for j in range(n-2):
        cnt1 = board[i][j] + board[i][j+1] + board[i][j+2]

        for a in range(n):
            for b in range(n-2):
                if i == a and (j <= b+2 and b <= j+2):
                    continue
            
                cnt2 = board[a][b] + board[a][b+1] + board[a][b+2]

                max_cnt = max(max_cnt, cnt1 + cnt2)

print(max_cnt)