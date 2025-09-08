from collections import deque
import sys
input = sys.stdin.readline

n, m, r = map(int, input().split())
graph = [[] for _ in range(n+1) ]
visited = [0] * (n + 1)
visited[r] = 1

for _ in range(m):
  u, v = map(int, input().split())
  graph[u].append(v)
  graph[v].append(u)

queue = deque([r])

# 오름차순 정렬
for i in range(1, n+ 1):
  graph[i].sort()


turn = 1

while queue:
  v = queue.popleft()
  for i in graph[v]:
    if visited[i]: continue
    turn += 1
    visited[i] = turn
    queue.append(i)

print(*visited[1:], sep="\n")