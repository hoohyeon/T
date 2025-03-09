n, m = map(int, input().split())

d = []
t = []
for _ in range(n):
    direction, time = input().split()
    d.append(direction)
    t.append(int(time))

d2 = []
t2 = []
for _ in range(m):
    direction, time = input().split()
    d2.append(direction)
    t2.append(int(time))

a = {}
b = {}

a_time, b_time = 0, 0
a_position, b_position = 0, 0

for i in range(n):
    if d[i] == 'R':
        for j in range(1, t[i]+1):
            a_position += 1
            a[a_time + j] = a_position
    else:
        for j in range(1, t[i]+1):
            a_position -= 1
            a[a_time + j] = a_position
    a_time += t[i]
    
for i in range(m):
    if d2[i] == 'R':
        for j in range(1, t2[i]+1):
            b_position += 1
            b[b_time + j] = b_position
    else:
        for j in range(1, t2[i]+1):
            b_position -= 1
            b[b_time + j] = b_position
    b_time += t2[i]

ans = -1

for time in range(1, len(a)+1):
    if a[time] == b[time]:
        ans = time
        break

print(ans)