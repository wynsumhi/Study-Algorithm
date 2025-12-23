T = int(input())


def factorial(num):
    if num <= 1:
        return 1
    else:
        return num * factorial(num - 1)


for tc in range(1, T + 1):
    N, M = map(int, input().split())

    result = int(factorial(M) // (factorial(N) * factorial(M - N)))

    print(result)