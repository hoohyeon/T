m = 5
name = []
height = []
weight = []

for _ in range(m):
    n, h, w = input().split()
    name.append(n)
    height.append(int(h))
    weight.append(float(w))

class Person:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

arr = []
for i in range(m):
    arr.append(Person(name[i], height[i], weight[i]))

arr.sort(key=lambda x: x.name)

print('name')
for person in arr:
    print(person.name, person.height, person.weight)

arr.sort(key=lambda x: -x.height)
print()
print('height')
for person in arr:
    print(person.name, person.height, person.weight)
