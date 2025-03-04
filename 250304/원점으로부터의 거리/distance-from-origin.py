n = int(input())
points = [(int(i), tuple(map(int, input().split()))) for i in range(n)]

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

points.sort(key=lambda p: (abs(p[1][0]) + abs(p[1][1])) )

for i in range(n):
    print(points[i][0] + 1)