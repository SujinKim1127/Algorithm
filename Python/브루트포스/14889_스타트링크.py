from itertools import combinations

import sys
input = sys.stdin.readline

n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]

pair = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        value = s[i][j] + s[j][i]
        pair[i][j] = value
        pair[j][i] = value

def team_score(team):
    score = 0
    for i , j in combinations(team, 2):
        score += pair[i][j]
    return score

ans = float("inf")
for start in combinations(range(1, n), n//2 - 1):
    start = (0, ) + start

    link = [x for x in range(n) if x not in start]

    diff = abs(team_score(start) - team_score(link))
    if diff == 0:
        ans = 0
        break
    ans = min(ans, diff)

print(ans)