
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])

        INF = 10**9
        answer = [[INF] * m for _ in range(n)]
        q = deque()
        dx = [-1, 1, 0, 0]
        dy = [0, 0, 1, -1]

    

        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    answer[i][j] = 0
                    q.append((i,j))

        while q:
            x, y = q.popleft()
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if 0 <= nx < n and 0 <= ny < m:
                    if answer[nx][ny] > answer[x][y] + 1:
                        answer[nx][ny] = answer[x][y] + 1
                        q.append((nx, ny))
                    
        return answer