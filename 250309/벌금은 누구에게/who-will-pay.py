n, m, k = map(int, input().split())

students = [0] * (n+1)
ans = -1

for i in range(m):
    number = int(input())
    students[number] += 1

    if students[number] >= k:
        ans = number
        break

print(ans)