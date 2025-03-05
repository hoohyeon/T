m1, d1, m2, d2 = map(int, input().split())

num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

days_of_week = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

start, end = d1, d2

for i in range(m1):
    start += num_of_days[i]

for i in range(m2):
    end += num_of_days[i]


start_day = days_of_week[(end-start) % 7]
print(start_day)