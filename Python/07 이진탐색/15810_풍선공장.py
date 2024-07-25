import sys
input = sys.stdin.readline

n, m = map(int, input().split())
times = list(map(int, input().split()))

l, r = 1, min(times) * m

while l <= r:
    mid = (l + r) // 2
    ballons = 0
    for i in range(n):
        ballons += (mid // times[i]) 
    
    if ballons < m:
        l = mid + 1
    else: r = mid - 1

print(l)