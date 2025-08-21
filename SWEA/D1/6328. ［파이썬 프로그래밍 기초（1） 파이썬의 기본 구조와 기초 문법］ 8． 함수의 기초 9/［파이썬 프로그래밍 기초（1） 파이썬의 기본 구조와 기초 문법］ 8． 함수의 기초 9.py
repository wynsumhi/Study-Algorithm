def longer(N: str, M: str):
    if len(N) > len(M):
        print(N)
    elif len(N) < len(M):
        print(M)
    else:
        print('길이가 같습니다.')

longer('one', 'three')