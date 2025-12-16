def find_dwarfs():

    arr = []

    for _ in range(9):
        arr.append(int(input()))

    total = sum(arr)

    for i in range(9):
        for j in range(i + 1, 9):
            if arr[i] + arr[j] == total - 100:
                # 큰 인덱스부터 제거 **
                arr.pop(j)
                arr.pop(i)
                arr.sort()

                for n in arr:
                    print(n)
                return

find_dwarfs()
