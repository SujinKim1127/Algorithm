from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]


def find_pos(graph, w, h):
    fires = deque()
    for i in range(h):
        for j in range(w):
            if graph[i][j] == "@": sang = (i, j)
            if graph[i][j] == "*": fires.append((i, j))

    return sang, fires

def solve_case(w, h, building):
    sang, fires = find_pos(building, w, h)

    fire_dist = [[-1] * w for _ in range(h)]
    qf = deque()
    for fy, fx in fires:    # 불 위치 먼저 표시
        fire_dist[fy][fx] = 0
        qf.append((fy, fx))

    while qf:
        y, x = qf.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= ny < h and 0 <= nx < w:
                if building[ny][nx] != '#' and fire_dist[ny][nx] == -1:
                    fire_dist[ny][nx] = fire_dist[y][x] + 1
                    qf.append((ny, nx))

    sy, sx = sang
    dist = [[-1] * w for _ in range(h)]
    qs = deque()
    dist[sy][sx] = 0
    qs.append((sy, sx))

    while qs:
        y, x = qs.popleft()
        # 지금 가장자리면 다음에 탈출 성공하니까
        if y == 0 or y == h - 1 or x == 0 or x == w - 1:
            return dist[y][x] + 1
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= ny < h and 0 <= nx < w:
                if building[ny][nx] != '#' and dist[ny][nx] == -1:
                    nd = dist[y][x] + 1
                    # 불이 안오거나                     불보다 내가 빠를때
                    if fire_dist[ny][nx] == -1 or fire_dist[ny][nx] > nd:
                        dist[ny][nx] = nd
                        qs.append((ny, nx))
    return "IMPOSSIBLE"


t = int(input())

for _ in range(t):
    w, h = map(int, input().split())
    building = [list(input().strip()) for _ in range(h)]
    print(solve_case(w, h, building))