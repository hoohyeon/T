m1, d1, m2, d2 = map(int, input().split())

num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

start, end = d1, d2

for i in range(m1):
    start += num_of_days[i]

for i in range(m2):
    end += num_of_days[i]

print(end-start+1)