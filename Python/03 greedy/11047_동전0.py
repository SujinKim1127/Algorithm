N, K = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(int(input()))

count = 0
# 내림차순
for x in range(N - 1, -1, -1):
    if K // arr[x] > 0:
        count += (K // arr[x])
        K = K % arr[x]

print(count)        