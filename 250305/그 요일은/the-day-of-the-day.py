m1, d1, m2, d2 = map(int, input().split())
A = input()

num_of_days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

days_of_week = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

start, end = d1, d2

for i in range(m1):
    start += num_of_days[i]

for i in range(m2):
    end += num_of_days[i]

cnt = 0
cnt += (end - start) // 7

remaining_days = (end - start) % 7

for i in range(remaining_days+1):
    if days_of_week[i % 7] == A:
        cnt += 1

print(cnt)