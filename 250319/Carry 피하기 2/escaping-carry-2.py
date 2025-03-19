n = int(input())

def f(x, y, z):

    while x > 0 or y > 0 or z > 0:

        x, dx = divmod(x, 10)
        y, dy = divmod(y, 10)
        z, dz = divmod(z, 10)

        if dx + dy + dz >= 10:
            return True
        
    return False

numbers = [int(input()) for _ in range(n)]

max_sum = -1

for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            if not f(numbers[i], numbers[j], numbers[k]):
                max_sum = max(max_sum, numbers[i]+numbers[j]+numbers[k])

print(max_sum)