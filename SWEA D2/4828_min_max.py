## 4828. [파이썬 S/W 문제해결 기본] 1일차 - min max
'''
[input]
3
5
477162 658880 751280 927930 297191
5
565469 851600 460874 148692 111090
10
784386 279993 982220 996285 614710 992232 195265 359810 919192 158175

[output]
#1 630739
#2 740510
#3 838110
'''

# 방법 1. 내장함수를 사용해도 된다면
# 1-1) 리스트를 구한 후 max min 함수를 활용하여 차이를 출력한다.
# 1-2) sorted 함수를 사용하여 정렬 후 최대 최소 차이값을 구한다.

# 방법 2. 내장함수를 사용하지 않는다면
# 2-1) 최댓값, 최소값을 임시로 지정한 후
# if 문을 사용하여 가장 큰 값과 가장 작은 값을 찾아 갱신해준다.
# 2-2) 정렬(버블정렬, 오름차순 이용)을 한 후
# 가장 끝쪽의 차이 - 가장 큰 수에서 가장 작은 수를 뺀다.


# 풀이 1. ----------------------------------------
# 1-1) max min 함수 활용
# T = int(input())
#
# for tc in range(1, T + 1):
#     N = int(input())
#
#     numbers = list(map(int, input().split()))
#     result = max(numbers) - min(numbers)
#     print(f'#{tc} {result}')


# 1-2) sorted 함수 활용
# T = int(input())
#
# for tc in range(1, T + 1):
#     N = int(input())
#
#     numbers = list(map(int, input().split()))
#     numbers.sort()
#     result = numbers[-1] - numbers[0]
#     print(f'#{tc} {result}')

## ** numbers.sort()는 None을 반환하기 때문에 **
## new_numbers = numbers.sort() 이딴건 없음 *** None임 ***

### list.sort() - 원본 리스트 자체를 정렬, 리스트 전용 메서드
### sorted(iterable) - 원본 그대로 두고 새로운 리스트 반환, 모든 iterable에 사용 가능


# 풀이 2. ----------------------------------------
# 2-1) 갱신하여 최소 최대값 구하기
# T = int(input())
#
# for tc in range(1, T + 1):
#     N = int(input())
#
#     numbers = list(map(int, input().split()))
#     min_num = numbers[0]
#     max_num = numbers[0]
#     for i in range(len(numbers)):
#         if numbers[i] < min_num:
#             min_num = numbers[i]
#         if numbers[i] > max_num:
#             max_num = numbers[i]
#         result = max_num - min_num
#     print(f'#{tc} {result}')

# 2-2) 버블 정렬 활용
# 버블 정렬을 활용하여 배열을 오름차순으로 정리하는 함수
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