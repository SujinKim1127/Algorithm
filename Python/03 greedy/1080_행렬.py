n, m = map(int, input().split())
A = [list(map(int, input())) for _ in range(n)]
B = [list(map(int, input())) for _ in range(n)]

def flip(i, j):
    for x in range(i, i+3):
        for y in range(j, j+3):
            A[x][y] = 1 - A[x][y]

count = 0
for i in range(n - 2):
    for j in range(m - 2):
        if A[i][j] != B[i][j]:
            flip(i, j)
            count += 1

if A == B: print(count)
else: print(-1)