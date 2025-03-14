a = input()

if '0' in a:
    for i in range(len(a)):
        if a[i] == '0':
            a = a[:i] + '1' + a[i+1:]
            break

else:
    a = a[:-1] + '0'
    
print(int(a, 2))