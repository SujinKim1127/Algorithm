import sys
input = sys.stdin.readline

n, m = map(int, input().split())
points = sorted(list(map(int, input().split())))

def pos(v, dir):
    left, right = 0, n-1
    while left <= right:
        mid = (left + right) // 2
        if(points[mid] > v):
            right = mid - 1
        elif points[mid] < v :
            left = mid + 1
        else: return mid
    if dir == 0: return left
    else: return right

for _ in range(m):
    l, r = map(int, input().split())
    lp = pos(l, 0)
    rp = pos(r, 1)
    print(rp - lp + 1)