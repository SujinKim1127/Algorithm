import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))

partSum = sum(arr[:k])
result = partSum
for i in range(0, n-k):
    partSum = partSum - arr[i] + arr[i+k]
    result = max(result, partSum)

print(result)