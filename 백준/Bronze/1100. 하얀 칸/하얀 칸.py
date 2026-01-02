count = 0
for row in range(8):
    line = input()
    for col in range(8):
        if (row + col) % 2 == 0 and line[col] == 'F':
            count += 1

print(count)