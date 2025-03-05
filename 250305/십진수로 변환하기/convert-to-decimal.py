binary = input()
decimal = 0

for i in range(len(binary)):
    decimal += 2 ** i * int(binary[::-1][i])

print(decimal)