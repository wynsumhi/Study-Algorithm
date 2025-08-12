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

# 결과 값 = 가장 큰 수와 가장 작은 수의 차이
# 버블 정렬을 이용하여 주어진 input 값을 오름차순 정렬을 한 후
# 가장 큰 수에서 가장 작은 수를 뺀다.

# for i in range()

T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    for _ in range(N):
        numbers = list(map(int, input().split()))
result = max(numbers) - min(numbers)
print(f'#{tc} {result}')
