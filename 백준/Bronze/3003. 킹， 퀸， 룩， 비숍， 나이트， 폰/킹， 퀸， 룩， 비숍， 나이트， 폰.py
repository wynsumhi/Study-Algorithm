standard = [1, 1, 2, 2, 2, 8]

current = list(map(int, input().split()))

result = [stand - cur for stand, cur in zip(standard, current)]

print(*result)