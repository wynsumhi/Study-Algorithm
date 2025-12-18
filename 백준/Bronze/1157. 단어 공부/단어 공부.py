from collections import Counter

word = input().strip().upper()

count = Counter(word)

max_count = max(count.values())

result = []
for char, cnt in count.items():
    if cnt == max_count:
        result.append(char)

if len(result) > 1:
    print('?')
else:
    print(result[0])