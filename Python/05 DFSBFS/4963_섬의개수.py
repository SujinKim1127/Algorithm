from collections import deque

while True: 
    w, h = map(int, input().split())
    if w == 0 and h == 0: break
    graph = []
    visited = [[False]  * w for _ in range(h)]
    for _ in range(h):
        graph.append(list(map(int, input().split())))

    dx = [-1, 1, 1, -1, 0, 0, 1, -1]
    dy = [0,0, -1, 1, -1, 1, 1, -1]

    def BFS(x, y):
        queue = deque()
        queue.append((x,y))
        while queue:
            (x, y) = queue.popleft()
            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]
                if  (0 <= nx <h) and (0 <= ny < w) and graph[nx][ny] == 1 :
                    graph[nx][ny] = -1
                    queue.append((nx, ny))

    cnt = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                BFS(i, j)
                cnt += 1

    print(cnt)



