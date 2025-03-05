N = input()

decimal = 0
for digit in N:
    decimal = decimal * 2 + int(digit)

decimal *= 17

binary_result = []

while decimal > 0:
    binary_result.append(str(decimal % 2))
    decimal //= 2

for i in binary_result[::-1]:
    print(i, end='')