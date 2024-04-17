from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

dx = [-1, 1, 2, 2, 1, -1, -2, -2]
dy = [2, 2, 1, -1, -2, -2, -1, 1]


def BFS(a, b):
    queue = deque()
    queue.append([a,b])
    while queue:
        x, y = queue.popleft()
        if [x,y] == end: return distance[x][y]
        else:
            for i in range(8):
                nx = x+dx[i]
                ny = y + dy[i]
                if (0<= nx < l) and (0<= ny < l) and distance[nx][ny] == 0:
                    queue.append([nx,ny])
                    distance[nx][ny] = distance[x][y] + 1

for _ in range(n):
    l = int(input())
    distance = [[0] * l for _ in range(l)]
    start = list(map(int, input().split()))
    end = list(map(int, input().split()))
    print(BFS(start[0], start[1]))