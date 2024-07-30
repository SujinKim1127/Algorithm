import math
import sys
input = sys.stdin.readline

t = int(input())

while t:
    t -= 1
    n = int(input())
    l, r, ans = 0, int(1e9), 0
    move = 1
    while l < r:
        mid = (l+r) // 2
        if mid * (mid + 1) // 2 <= n:
            ans = mid
            l = mid + 1
        else: r = mid

    print(ans)
        
