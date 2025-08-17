## 4834. [파이썬 S/W 문제해결 기본] 1일차 - 숫자 카드

'''
[input]
3
5
49679
5
08271
10
7797946543

[output]
#1 9 2
#2 8 1
#3 7 3
'''

# 0 ~ 9 까지 적힌 숫자 N장의 카드 중
# 가장 많은 카드에 적힌 숫자와 카드가 몇 장인지!
## 카운트 정렬을 사용하여 가장 많은 카운트를 쌓은 카드의 숫자와 장수를 구한다.

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    cards = list(map(int, input()))

    # 가장 많은 카드(찾는 카드의 숫자)
    max_card = 0

    # 가장 많은 카드의 장수
    max_count = 0

    # 카드 수를 저장하는 리스트(카운트 배열) - [0, 0, 0, 0...]
    num_of_cards = [0] * 10

    # 주어진 카드의 각각을 순회하며
    for card in cards:
        # 만약 임의 생성한 카운트 배열의 card 원소가 일치하면
        num_of_cards[card] += 1

    # 생성한 카운트 배열의 길이만큼 순회하며
    for i in range(len(num_of_cards)):
        # 카운트 배열의 인덱스에 쌓인 수를 가장 많은 카드의 장수로 누적
        if max_count < num_of_cards[i]:
            max_count = num_of_cards[i]
            # 가장 많은 카드에 적힌 수 = 카운팅 배열의 인덱스
            max_card = i
        # ** 같은 개수라면 더 큰 숫자를 선택
        elif num_of_cards[i] == max_count and i > max_card:
            max_card = i

    print(f'#{tc} {max_card} {max_count}')