a = input()

for i in range(len(a)):
    if a[i] == '0':
        a = a[:i] + '1' + a[i+1:]
        break

print(int(a, 2))