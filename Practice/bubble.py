## 버블 정렬

'''
input
numbers = [64, 13, 9, 62, 3]

output
[3, 9, 13, 62, 64]
'''

# 버블 정렬을 이용한 함수
def bubble_sort(numbers):
    # 주어진 numbers의 길이에서 1을 뺸 횟수만큼 반복(마지막 요소는 자동으로 정렬되므로)
    # i는 비교 범위 끝부터 점점 줄어들게 순회 - i: i, i-1, i-2... 2, 1, 0
    # 맨 뒤 값은 이미 정렬된 상태이기 때문에
    # 비교 범위를 줄여나가면서 연산을 줄임(i는 범위 끝 인덱스를 의미)
    for i in range(len(numbers) - 1, 0, -1):
        # 0 ~ i 까지 반복할 인덱스 j
        for j in range(0, i):
            # 현재 값이 다음 값보다 크면 위치를 교환 (오름차순 정렬)
            if numbers[j] > numbers[j + 1]:
                # 튜플 언패킹을 이용해 두 값 교환
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

    # 모든 비교가 끝난 후 정렬된 리스트 반환
    return numbers

# 임의의 배열
numbers = [64, 13, 9, 62, 3]
# 함수 호출 후 결과 저장
sorted_numbers = bubble_sort(numbers)
# 정렬 결과 출력
print(f'정렬 후: {sorted_numbers}')
