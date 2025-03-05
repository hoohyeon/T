n = int(input())

if n == 0:
    print(0)
else:
    digits = []

    while n >= 1:
        digits.append(n % 2)
        n //= 2

    for digit in reversed(digits):
        print(digit, end='')