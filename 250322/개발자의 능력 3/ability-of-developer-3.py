scores = list(map(int, input().split()))

min_gap = sum(scores)

for i in range(4):
    for j in range(i, 5):
        for k in range(j, 6):
            c_sum = scores[i] + scores[j] + scores[k]

            gap = abs(c_sum - (sum(scores) - c_sum))

            min_gap = min(min_gap, gap) 

print(min_gap)