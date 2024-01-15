import sys
input = sys.stdin.readline

M, N = map(int, input().split())
L = list(map(int, input().split()))

result = 0
left = 1
right = max(L)

while left <= right:
    total = 0
    mid = (left + right) // 2

    for x in L:
        if x >= mid:
            total += (x // mid)
    if total >= M:
        left = mid + 1
        result = max(result, mid)
    else:
        right = mid - 1

print(result)