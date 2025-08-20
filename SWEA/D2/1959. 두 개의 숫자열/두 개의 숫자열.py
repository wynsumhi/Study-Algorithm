
import math

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    Ai = list(map(int, input().split()))
    Bj = list(map(int, input().split()))

    # 문제점
    # ** 두배열중 어떤 배열의 길이가 더 큰지는 모른다.

    # 짧은 배열과 긴 배열 구분
    if len(Ai) <= len(Bj):
        shorter, longer = Ai, Bj
    else:
        shorter, longer = Bj, Ai

    S = len(shorter)
    L = len(longer)

    max_total = -10 ** 18

    # 슬라이딩 범위: 0 ~ (L - S)
    for start in range(L - S + 1):
        total = 0
        for i in range(S):
            total += shorter[i] * longer[start + i]  # index 초과 없음
        max_total = max(max_total, total)

    print(f'#{tc} {max_total}')