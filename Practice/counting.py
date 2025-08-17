## 카운팅 정렬

'''
[input]
arr = [0, 4, 1, 3, 1, 2, 4, 1]

[output]
[0, 1, 1, 1, 2, 3, 4, 4]
'''
# 1. 데이터 범위 크기(k+1)의 배열을 준비
# 2. 각 숫자의 빈도(등장 횟수)를 기록
# 3. 누적합으로 바꿔서 “이 숫자가 들어갈 자리” 계산
# 4. 입력 배열을 뒤에서부터 순회하며 결과 배열에 채움
# 5. 결과 반환

# 0 ~ K 까지의 정수를 가진 배열 정렬
def counting_sort(input_arr, k): # (주어진 배열, 가장 큰 수 K)
    # 1. K + 1 크기의 카운팅 배열을 0으로 생성 (인덱스 0부터 K까지)
    counting_arr = [0] * (k + 1) # 각 인덱스는 숫자 / 값은 그 숫자가 몇 번 나왔는지(빈도)

    # 2. 주어진 배열의 num을 순회하며 각 원소의 빈도수를 카운팅 배열에 기록
    for num in input_arr:
        counting_arr[num] += 1

    # 3. 누적 합을 계산하여 각 원소가 정렬된 배열 내에서 차지할 위치 결정
    for i in range(1, k + 1):
        counting_arr[i] += counting_arr[i - 1]

    # 결과 배열을 입력 배열과 같은 크기로 생성
    result_arr = [0] * len(input_arr)

    # 4. 입력배열을 역순으로 순회하며 결과 배열에 채움
    for num in reversed(input_arr):
        counting_arr[num] -= 1
        result_arr[counting_arr[num]] = num

    return result_arr

arr = [0, 4, 1, 3, 1, 2, 4, 1]
print('정렬 결과:', counting_sort(arr, 5))  # [0, 1, 1, 1, 2, 3, 4, 4]