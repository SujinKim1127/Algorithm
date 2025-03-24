import sys
input = sys.stdin.readline

t= int(input())
for _ in range(t):
    n = int(input())
    arr = sorted(list(map(int, input().split())))
    ans = 0
    for i in range(len(arr) - 2):
        for j in range(i+2, len(arr)):
            left = i
            right = j
            target = (arr[left] + arr[right]) / 2
            while (left <= right):
                mid_idx = (left + right) // 2
                if arr[mid_idx] == target: ans += 1; break
                elif arr[mid_idx] < target: left = mid_idx + 1
                elif arr[mid_idx] > target: right = mid_idx - 1

    print(ans)