word = input().strip()
n = len(word)
result = []

for i in range(1, n-1):
    for j in range(i+1, n):
        part1 = word[:i][::-1]
        part2 = word[i:j][::-1]
        part3 = word[j:][::-1]
        result.append(part1 + part2 + part3)

print(min(result))