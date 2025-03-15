n = int(input())
checkpoint = []

for _ in range(n):
    checkpoint.append(list(map(int, input().split())))

def manhattan(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

total_distance = sum(manhattan(checkpoint[i], checkpoint[i+1]) for i in range(n-1))

min_distance = int(1e9)

for j in range(1, n-1): # j번째 건너뛰기
    saved_distance = manhattan(checkpoint[j-1], checkpoint[j]) + manhattan(checkpoint[j], checkpoint[j+1])
    new_distance = total_distance - saved_distance + manhattan(checkpoint[j-1], checkpoint[j+1])
    min_distance = min(min_distance, new_distance)

print(min_distance)