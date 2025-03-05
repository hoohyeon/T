a, b = map(int, input().split())
n = input()

decimal = 0
for i in n:
    decimal = decimal * a + int(i)

arr = []
while decimal > 0:
    arr.append(decimal % b)
    decimal //= b

for i in arr[::-1]:
    print(i, end='')