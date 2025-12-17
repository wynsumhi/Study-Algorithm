arr = [1, 1, 2, 2, 2, 8]

find = list(map(int, input().split()))

result = []

for i in range(6):
    result.append(arr[i] - find[i])

print(*result)
