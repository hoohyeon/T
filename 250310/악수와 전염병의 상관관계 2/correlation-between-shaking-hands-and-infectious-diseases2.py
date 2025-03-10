N, K, P, T = map(int, input().split())
handshakes = [tuple(map(int, input().split())) for _ in range(T)]

infected = [0] * (N+1)  # 감염 여부
count = [0] * (N+1)     # 전염 횟수

infected[P] = 1         # 감염 시작

handshakes.sort()
for h in handshakes:
    if (infected[h[1]] == 1 or infected[h[2]] == 1) and (count[h[1]] < K and count[h[2]] < K) :
        infected[h[1]] = 1
        infected[h[2]] = 1
        count[h[1]] += 1
        count[h[2]] += 1

for person in infected[1:]:
    print(person, end='')