n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

line = [0] * 200

for segment in segments:
    for i in range(segment[0], segment[1]+1):
        line[i] += 1

print(max(line))