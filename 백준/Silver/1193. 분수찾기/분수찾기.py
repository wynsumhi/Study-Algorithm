X = int(input())

# X가 속한 대각선 번호
diagonal = 1
while diagonal * (diagonal + 1) // 2 < X:
    diagonal += 1

# 해당 대각선에서의 위치 (1부터 시작)
# 이전 대각선까지의 분수 개수
prev_count = (diagonal - 1) * diagonal // 2
# 현재 대각선에서 몇 번째인지
position = X - prev_count

if diagonal % 2 == 1:
    num = diagonal - position + 1
    den = position
else:
    num = position
    den = diagonal - position + 1

print(f"{num}/{den}")