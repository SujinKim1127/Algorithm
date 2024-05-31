n, d = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

first = 0
last = 0
length = 0

while first < n and last < n:
    if arr[last] - arr[first] <= d:
        length = max(length, last - first + 1)
        print("<=", length, arr[last], arr[first])

        last += 1
    else:
        first += 1
        print("++first")

print(n - length)