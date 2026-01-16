N = int(input())
F = int(input())

base = (N // 100) * 100

for i in range(100):
    if (base + i) % F == 0:
        print(str(i).zfill(2))
        break