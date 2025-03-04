a, b, c = map(int, input().split())

start = 24 * 60 * 11 + 60 * 11 + 11
end = 24 * 60 * a + 60 * b + c

if end - start > 0:
    print(end-start)
else:
    print(-1)