n, m = map(int, input().split())
a, b = [], []
a_position, b_position = 0, 0

for _ in range(n):
    t, d = input().split()
    t = int(t)

    for i in range(t):
        if d == 'R':
            a_position += 1
        
        else:
            a_position -= 1

        a.append(a_position)

for _ in range(m):
    t, d = input().split()
    t = int(t)

    for i in range(t):
        if d == 'R':
            b_position += 1
        
        else:
            b_position -= 1

        b.append(b_position)

max_len = max(len(a), len(b))

while len(a) < max_len:
    a.append(a[-1])

while len(b) < max_len:
    b.append(b[-1])

cnt = 0
for i in range((min(len(a), len(b)))-1):
    if a[i] != b[i] and a[i+1] == b[i+1]:
        cnt += 1

print(cnt)