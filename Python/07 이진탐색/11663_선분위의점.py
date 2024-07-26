import sys
input = sys.stdin.readline

n, m = map(int, input().split())

point = sorted(list(map(int, input().split())))

def bs(v, dir):
    left, right = 0, n-1
    while left <= right:
        mid = (left + right) // 2
        if point[mid] > v:
            right = mid - 1
        elif point[mid] < v:
            left = mid + 1
        else: return mid
    if dir == 0: return left
    else: return right

for _ in range(m):
    l, r = map(int, input().split())
    li, ri = bs(l, 0), bs(r, 1)
    print(ri - li + 1)