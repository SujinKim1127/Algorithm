n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

def dfs(x, y):
    # 주어진 범위를 넘어가면 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    
    # 현재 노드를 방문안한 경우
    if graph[x][y] == 0 :
        # 해당 노드 방문 처리
        graph[x][y] = 1
        # 상 하 좌 우 위치 재귀로 호출
        dfs(x - 1, y)   # 좌    
        dfs(x, y - 1)   # 상
        dfs(x + 1, y)   # 우
        dfs(x, y + 1)   # 하
        print("true")
        return True
    print("False")
    
    return False

# 모든 위치(노드)에 음료수 채우기
result = 0
for i in range(n):
    for j in range(m): 
        # 현재 위치에서 DFS 수행
        if dfs(i, j) == True:
            print("---------------TRUE-------------", i, j)
            result += 1

print(result)