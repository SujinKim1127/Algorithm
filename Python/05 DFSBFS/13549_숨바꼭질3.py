from collections import deque
import sys
input = sys.stdin.readline
MAX = 100000
INF = 10**9
n, k = map(int, input().split())
dist = [INF] * (MAX + 1)
dist[n] = 0


q = deque([n])

while q:
    x = q.popleft()
    if x == k: 
        print(dist[x])
        break

    nx = 2 * x
    if nx <= MAX and dist[nx] > dist[x]:
        dist[nx] = dist[x]
        # print(nx, "-", dist[nx])
        q.appendleft(nx)
    
    nx = x - 1
    if nx >= 0 and dist[nx] > dist[x] + 1:
        dist[nx] = dist[x] + 1
        # print(nx, "-", dist[nx])
        q.append(nx)
    
    nx = x + 1
    if nx <= MAX and dist[nx] > dist[x] + 1:
        dist[nx] = dist[x] + 1
        # print(nx, "-", dist[nx])
        q.append(nx)
