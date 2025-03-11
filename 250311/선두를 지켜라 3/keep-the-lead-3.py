n, m = map(int, input().split())

a_now, b_now = 0, 0
a_move, b_move = [], []

for _ in range(n):
    v, t = map(int, input().split())

    for _ in range(t):
        a_now += v        
        a_move.append(a_now)

for _ in range(m):
    v, t = map(int, input().split())

    for _ in range(t):
        b_now += v        
        b_move.append(b_now)

lead = -2
count = 0
for time in range(len(a_move)):
    if a_move[time] - b_move[time] > 0:
        new_lead = 1

    elif a_move[time] - b_move[time] < 0:
        new_lead = -1

    else:
        new_lead = 0

    if lead != new_lead:
        count += 1
        lead = new_lead

print(count)