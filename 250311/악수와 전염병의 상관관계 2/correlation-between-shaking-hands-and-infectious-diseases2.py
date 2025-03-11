N, K, P, T = map(int, input().split())
handshakes = [tuple(map(int, input().split())) for _ in range(T)]

infected = [0] * (N+1)  # 감염 여부
count = [0] * (N+1)     # 전염 횟수

infected[P] = 1         # 감염 시작

handshakes.sort()

for t, x, y in handshakes:
    if infected[x] and count[x] < K:
        infected[y] = 1

    elif infected[y] and count[y] < K:
        infected[x] = 1

    count[x] += 1
    count[y] += 1
    

for person in infected[1:]:
    print(person, end='')