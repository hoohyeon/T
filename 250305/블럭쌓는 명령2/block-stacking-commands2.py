n, k = map(int, input().split())
commands = [tuple(map(int, input().split())) for _ in range(k)]

blocks = [0] * n

for command in commands:
    for i in range(command[0], command[1]+1):
        blocks[i] += 1

print(max(blocks))