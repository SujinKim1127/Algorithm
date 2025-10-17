import sys
input = sys.stdin.readline

n, m = map(int, input().split())
trees = list(map(int, input().split()))
# 10 15 17 20

left = 1
right = max(trees)
ans = 0

while left <= right:
    mid = (left + right) // 2
    cut = 0
    for tree in trees:
        if tree - mid > 0: cut += tree - mid
    
    if cut >= m:
        ans = mid
        left = mid + 1

    elif cut < m:
        right = mid - 1

print(ans)


