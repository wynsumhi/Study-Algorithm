## 6249. [파이썬 프로그래밍 기초(1) 파이썬의 기본 구조와 기초 문법]
## 7. 흐름과 제어 - 반복 10

nums = '11'

# for i in range(10):
#     print(i, end=' ')

# 카운트가 생각이 안났다...
count = [0] * 10

for num in nums:
    count[int(num)] += 1

print(' '.join(str(i) for i in range(10)))
print(' '.join(str(c) for c in count))

