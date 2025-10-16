nA, nB = map(int, input().split())
# 이진탐색
A = list(map(int, input().split()))
B = sorted(map(int, input().split()))

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False

result = []
for a in A:
    if not binary_search(B, a): result.append(a)

result.sort()
print(len(result))
if result: print(*result)


# 해시 set 으로
A = set(map(int, input().split()))
B = set(map(int, input().split()))

diff = sorted(A - B)
print(len(diff))
if diff: print(*diff)



