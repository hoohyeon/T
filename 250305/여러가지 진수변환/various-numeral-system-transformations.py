N, B = map(int, input().split())
arr = []

while True:
    arr.append(N % B)
    N //= B

    if N == 0:
        break

for i in arr[::-1]:
    print(i, end='')