N = int(input())
arr = list(map(int, input().split()))

start = 0
end = N - 1
result = 2000000000
first = 0
second = 0

while start < end:
    current = arr[start] + arr[end]
    if abs(current) <= abs(result):
        result = arr[start] + arr[end]
        first = arr[start]
        second = arr[end]
    if current < 0:
        start += 1
    else:
        end -= 1

print(first, second)