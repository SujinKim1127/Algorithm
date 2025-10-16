t = int(input())
for _ in range(t):
    n = int(input())
    jus = list(map(int, input().split()))

    jus.reverse()
    big = jus[0]
    result = 0
    for i in range(1, n):
        if big > jus[i]:
            result += big - jus[i]
        else: big = jus[i]
    
    print(result)
