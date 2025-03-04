n = int(input())
students = [
    (h, w, i + 1)
    for i, (h, w) in enumerate([tuple(map(int, input().split())) for _ in range(n)])
]

class Student:
    def __init__(self, height, weight, number):
        self.height = height
        self.weight = weight
        self.number = number

arr = []
for student in students:
    arr.append(Student(student[0], student[1], student[2]))

arr.sort(key=lambda x: (x.height, -x.weight))

for student in arr:
    print(student.height, student.weight, student.number)
