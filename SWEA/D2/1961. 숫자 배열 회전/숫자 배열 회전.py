T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    arr90 = []
    arr180 = []
    arr270 = []

    # 90도
    for c in range(N):
        for r in range(N - 1, -1, -1):
            arr90.append(arr[r][c])

    # 180도
    for r in range(N - 1, -1, -1):
        for c in range(N - 1, -1, -1):
            arr180.append(arr[r][c])

    # 270도
    for r in range(N - 1, -1, -1):
        for c in range(N):
            arr270.append(arr[c][r])

    print(f'#{tc}')
    for i in range(0, N * N, N):
        print(''.join(map(str, arr90[i:i + N])) , end=' ')
        print(''.join(map(str, arr180[i:i + N])) , end=' ')
        print(''.join(map(str, arr270[i:i + N])))
