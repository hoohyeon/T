a, b, c, d = map(int, input().split())

start = 60 * a + b
end = 60 * c + d

print(end - start)