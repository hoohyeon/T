n = int(input())

people = []

for _ in range(n):
    c, a = input().split()
    people.append((int(c), a))

people.sort()

max_len = 0
for i in range(n):
    cnt_g, cnt_h = 0, 0
    for j in range(i, n):
        if people[j][1] == 'G':
            cnt_g += 1
        elif people[j][1] == 'H':
            cnt_h += 1

        if cnt_g == cnt_h or cnt_g == 0 or cnt_h == 0:
            max_len = max(max_len, people[j][0] - people[i][0])
print(max_len)