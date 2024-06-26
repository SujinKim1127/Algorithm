import sys
input = sys.stdin.readline


n, m = map(int, input().split())
arr = list(map(int, input().split()))

prefix_sum = [0]
temp = 0
for i in arr:
    temp += i
    prefix_sum.append(temp)

for i in range(m):
    start, end = map(int, input().split())
    print(prefix_sum[end] - prefix_sum[start - 1])