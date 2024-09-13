import sys
input = sys.stdin.readline

n, k = map(int, input().split(' '))
arr = list(map(int, input().split(' ')))

part_sum = sum(arr[0:k])
result = part_sum

for i in range(0, n-k):
    part_sum = part_sum - arr[i] + arr[i+k]
    result = max(part_sum, result)

print(result)