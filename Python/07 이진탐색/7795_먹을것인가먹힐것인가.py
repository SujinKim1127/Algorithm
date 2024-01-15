import sys
input = sys.stdin.readline

t = int(input())

def binary_search(array, target, start, end, count):
    if start>end:
        return count
    mid = (start + end) // 2
    if target > array[mid]:
        return binary_search(array, target, mid + 1, end, mid)
    else:
        return binary_search(array, target, start, mid - 1, count)

for _ in range(t):
    m, n = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()


    result = 0
    for x in a:
        result += binary_search(b, x, 0, n - 1, -1) + 1

    print(result)