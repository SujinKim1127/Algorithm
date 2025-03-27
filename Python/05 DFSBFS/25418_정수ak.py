from collections import deque
import sys
input = sys.stdin.readline

A, K = map(int, input().split())


q = deque([A])
v = {A:0}
while q:
    target = q.popleft()
    if target == K: break
    for x in [target + 1, target * 2]:
        if x in v or x > K: continue
        v[x] = v[target] + 1
        q.append(x)

print(v[K])
