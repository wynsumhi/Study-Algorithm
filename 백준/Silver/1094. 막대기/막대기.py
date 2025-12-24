X = int(input())

sticks = [64]

while sum(sticks) > X:
    # 가장 짧은 막대를 절반으로 자름
    shortest = min(sticks)
    sticks.remove(shortest)
    half = shortest // 2

    # 절반 하나를 버려도 되는지 확인
    if sum(sticks) + half >= X:
        # 한 쪽만 추가
        sticks.append(half)
    else:
        # 양쪽 다 추가
        sticks.append(half)
        sticks.append(half)

print(len(sticks))