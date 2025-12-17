N, M = map(int, input().split())

matrix_a = [list(map(int, input().split())) for _ in range(N)]
matrix_b = [list(map(int, input().split())) for _ in range(N)]

for row_a, row_b in zip(matrix_a, matrix_b):
    print(*[a + b for a, b in zip(row_a, row_b)])