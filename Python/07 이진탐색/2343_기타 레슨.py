N, M = map(int, input().split())
arr = list(map(int, input().split()))

answer = 0
start, end = max(arr), sum(arr)

while start <= end:
    mid = (start + end) // 2
    count = 0
    sum = 0
    for x in range(0, N):
        if sum + arr[x] > mid:
            count += 1
            sum = 0
        sum += arr[x]
    if sum: count += 1

    if count > M:
        start = mid + 1
    else:
        end = mid - 1
        answer = mid


print(answer)

