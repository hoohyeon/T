n = int(input())
students = [
    (h, w, i + 1)
    for i, (h, w) in enumerate([tuple(map(int, input().split())) for _ in range(n)])
]

class Student:
    def __init__(self, number, height, weight):
        self.height = height
        self.weight = weight
        self.number = number

students.sort(key=lambda x: (x[0], -x[1]))

for student in students:
    print(student[0], student[1], student[2])
