def bubble_sort(array):
    # 리스트 길이에서 1을 뺀 만큼 반복(마지막 요소는 자동 정렬)
    # i는 비교 범위의 끝 인덱스(역순으로 점점 줄어듬)
    for i in range(len(array) - 1, 0, -1):
        # 비교할 값의 인덱스 j (0부터 i-1까지) - 내부 반복
        for j in range(i):
            # 현재 값이 다음 값보다 크면 위치를 교환(오름차순 정렬)
            if array[j] > array[j + 1]:
                # 튜플 언패킹을 이용해 두 값 교환
                array[j], array[j + 1] = array[j + 1], array[j]

    # 모든 비교가 끝난 후 정렬된 리스트 반환
    return array

T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    numbers = list(map(int, input().split()))
    sorted_numbers = bubble_sort(numbers)
    result = sorted_numbers[-1] - sorted_numbers[0]
    print(f'#{tc} {result}')