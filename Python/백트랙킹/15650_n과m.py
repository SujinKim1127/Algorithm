n, m = map(int, input().split())
path = []
def dfs(start):
    if len(path) == m:
        print(*path)
        return
    
    for x in range(start, n + 1):
        path.append(x)
        dfs(x + 1)
        # print("pop!")
        path.pop()

dfs(1)

# 콤비네이션 풀이
from itertools import combinations

N, M = map(int, input().split())

for comb in combinations(range(1, N+1), M):
    print(*comb)