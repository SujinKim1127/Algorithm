import sys
input = sys.stdin.readline

n , m = map(int, input().split())
times = list(map(int, input().split()))

l, r = 1, min(times) * m

while l <= r:
    mid = (l+r) // 2
    count = 0
    for x in times:
        count += mid // x
    if count >= m:
        r = mid - 1
    else: l = mid + 1

print(l)