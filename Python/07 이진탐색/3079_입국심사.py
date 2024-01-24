import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr =[]
for _ in range(N):
    arr.append(int(input()))

left = min(arr)
right = max(arr) * M
answer = right

while left <= right:
    mid = (left + right) // 2
    total = 0
    for x in arr:
        total += mid // x
    if total >= M:
        right = mid - 1
        answer = min(mid, answer)
    else:
        left = mid + 1


print(answer)