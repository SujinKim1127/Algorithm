n = int(input())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

small = min(map(min,graph))
big = max(map(max,graph))

# 높이별 체크
def check(graph, h):
    visit = [[1] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if graph[i][j] > h:
                visit[i][j] = 0
    return visit


def dfs(height, x, y, h):
    # 주어진 범위를 넘어가면 종료
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False
    
    # 현재 노드를 방문안한 경우
    if height[x][y] == 0 :
        # 해당 노드 방문 처리
        height[x][y] = 1
        # 상하좌우 위치재귀로 호출
        dfs(height, x-1, y, h)
        dfs(height, x, y - 1, h)
        dfs(height, x + 1, y, h)
        dfs(height, x, y + 1, h)
        return True
    return False

result = [0] * big

for h in range(big):
    print("height", h)
    height = check(graph, h)
    for i in range(n):
        for j in range(n):
            # 현재 위치에서 DFS 수행
            if dfs(height, i, j, h) == True:
                result[h] += 1
    
print(max(result))

