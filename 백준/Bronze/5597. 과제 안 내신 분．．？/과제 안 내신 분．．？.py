count  = [0] * 30
for c in range(30):
    count[c] = c + 1

for _ in range(28):
    n = int(input())
    if n in count:
        count.remove(n)

for i in range(2):
    print(count[i])