n = int(input())
sequence = list(map(int, input().split()))

class Number:
    def __init__(self, value, index):
        self.value = value
        self.index = index

numbers = [Number(value, index) for index, value in enumerate(sequence)]

numbers.sort(key=lambda x: x.value)

new_positions = [0] * n

for new_index, num in enumerate(numbers):
    new_positions[num.index] = new_index + 1

print(*new_positions)