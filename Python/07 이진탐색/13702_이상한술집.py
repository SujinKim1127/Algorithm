import sys
input = sys.stdin.readline

n, k = map(int, input().split())

water = []
for _ in range(n):
    water.append(int(input()))

left = 1
right = max(water)

result = 0

while (left <= right):
    mid = (left + right) // 2 
    count = 0
    count = sum( i // mid for i in water)
    if (count >= k):
        left = mid + 1
        result = mid
    elif (count < k):
        right = mid - 1

print(result)