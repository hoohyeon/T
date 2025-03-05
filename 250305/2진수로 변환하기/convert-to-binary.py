n = int(input())
digits = []

while n >= 1:
    digits.append(n % 2)
    n //= 2

for digit in digits[::-1]:
    print(digit, end='')