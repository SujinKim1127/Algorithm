T = int(input())
for _ in range(T):
    N = int(input())
    cnt = 1
    data = []
    for _ in range(N):
        a, b = map(int, input().split())
        data.append((a,b))
    data.sort(key = lambda x: x[0])     # 서류 순위로 정렬
    min = data[0][1]
    for x in range(1, N):
        if min > data[x][1]: 
            cnt += 1
            min = data[x][1]
    print(cnt)