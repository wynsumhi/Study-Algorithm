T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    
    result = pow(a, b, 10)
    
    if result == 0:
        result = 10
    
    print(result)