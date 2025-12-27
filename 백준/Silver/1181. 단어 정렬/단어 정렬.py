n = int(input())
words = set()

for _ in range(n):
    words.add(input().strip())

    
words = sorted(words, key=lambda x: (len(x), x))

for word in words:
    print(word)