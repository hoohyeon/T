n = int(input())
x = []
dir = []
for _ in range(n):
    xi, di = input().split()
    x.append(int(xi))
    dir.append(di)

c = [0] * 2000
start = 1000

for i in range(n):
    if dir[i] == 'R': # 오른쪽
        for j in range(start, start + x[i]):
            c[j] += 1
        
        start += x[i]
    else:
        for j in range(start -1, start - x[i] - 1, -1):
            c[j] += 1
    
        start -= x[i]

print(sum(x >= 2 for x in c))