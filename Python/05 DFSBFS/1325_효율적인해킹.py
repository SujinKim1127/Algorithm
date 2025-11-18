from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    A, B = map(int, input().split())
    # B가 해킹되면 A도 해킹 가능하니까
    graph[B].append(A)


def BFS(start):
    visited = [False] * (n + 1)
    queue = deque([start])
    visited[start] = True
    cnt = 1

    while queue:
        x = queue.popleft()
        for next in graph[x]:
            if not visited[next]:
                visited[next] = True
                cnt += 1
                queue.append(next)

    return cnt

maxCount = 0
answer = [0] * (n + 1)

for start in range(1, n + 1):
    count = BFS(start)
    maxCount = max(maxCount, count)
    answer[start] = count

for i in range(1, n + 1):
    if answer[i] == maxCount:
        print(i, end = " ")