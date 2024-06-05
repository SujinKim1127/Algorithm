t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    arr = list(enumerate(list(map(int, input().split()))))

    find = arr[m]
    idx = 0
    while arr:
        big = max([i[1] for i in arr])
        if arr[0][1] == big:
            now = arr.pop(0)
            idx += 1
            if now == find:
                print(idx)
                break
        else:
            now = arr.pop(0)
            arr.append(now)
