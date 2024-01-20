import math, sys
input = sys.stdin.readline
N, M = map(int, input().split())
arr = []
for _ in range(M):
    arr.append(int(input()))

answer = 999999999

start = 1
end = max(arr)

while start <= end:
    mid = (start + end) // 2
    count = 0
    for x in arr:
        count += math.ceil(x / mid)
    if count > N: 
        start = mid + 1
    else: # count <= N: 
        end = mid - 1
        answer = min(answer, mid)


print(answer)       