n, m = map(int, input().split())
a_position, b_position = 0, 0
a, b = [], []
cnt = 0

for _ in range(n):
    v, t = map(int, input().split())
    for _ in range(t):
        a_position += v
        a.append(a_position)


for _ in range(m):
    v, t = map(int, input().split())
    for _ in range(t):
        b_position += v
        b.append(b_position)

leader = -1

for i in range(len(a)):
    if a[i] > b[i]:
        if leader != 0:
            cnt += 1
            leader = 0
    elif a[i] < b[i]:
        if leader != 1:
            cnt += 1
            leader = 1
print(cnt-1)