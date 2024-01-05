n = int(input())
card = list(map(int, input().split()))
card.sort()
m = int(input())
request = list(map(int, input().split()))

def binary_search(array, target, start, end):
    if start > end:
        return 0
    mid = (start + end) // 2
    print("mid", mid)
    if array[mid] == target:
        print(target, start, end)
        return 1
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)

result = []
for x in request:
    result.append(binary_search(card, x, 0, n - 1))

print(*result)