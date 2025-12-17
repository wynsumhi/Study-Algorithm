students = set(range(1, 31))

for _ in range(28):
    n = int(input())
    students.discard(n)

result = sorted(students)
print(result[0])
print(result[1])