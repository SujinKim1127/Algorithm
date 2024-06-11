from collections import deque
import sys
input=sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    graph = [[] for _ in range(n + 1)]
    arr = list(map(int, input().split()))
    for x in range(1, n+1):
        graph[x].append(arr[x-1])

    visited = [False for _ in range(n+1)]

    def BFS(node):
        queue = deque()
        queue.append(node)
        visited[node] = True
        while queue:
            x = queue.popleft()
            for i in graph[x]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True

    cnt = 0

    for i in range(1, n+1):
        if not visited[i]:
            BFS(i)
            cnt += 1

    print(cnt)