n, m = map(int, input().split())

result = []

for i in range(n):
    arr = list(map(int, input().split()))
    arr.sort()
    result.append(arr[0])

result.sort(reverse=True)

print(result[0])


## answer
n, m = map(int, input().split())

result = 0

for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)
    result = max(result, min_value)

print(result)