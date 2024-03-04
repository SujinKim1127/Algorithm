from collections import Counter ## 최빈값 구하기 위해
import sys
input=sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
print(round(sum(arr)/n))
arr.sort()
print(arr[n//2])

# 최빈값
counter = Counter(arr)
value = counter.most_common(2)
if len(value) > 1:
    if value[0][1] == value[1][1]: print(value[1][0])
    else: print(value[0][0])
else: print(arr[0])

print(max(arr) - min(arr))