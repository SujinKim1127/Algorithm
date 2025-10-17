from collections import deque

def solution(L, R, D, F, G, T, C, B, W, E):
    
    arr = [0] + [1] * (L - 1)
    for i in range(R):
        arr[D[i]] = (F[i], G[i])   
    for i in range(T):
        arr[C[i]] = -B[i]
    for i in range(W):
        arr[E[i]] = 0

    dist = [-1] * (L + 1)
    q = deque([1])
    dist[1] = 0

    def next_moves(x):
        cell = arr[x]
        if isinstance(cell, tuple): # 토끼 
            f, g = cell
            return [x + f, x + g]
        elif cell < 0:  # 거북이
            return [x + cell]
        elif cell == 0:
            return [cell]
        else:           # 빈칸
            return [x + 1]

    while q:
        x = q.popleft()
        if x == L: return dist[x]

        for nx in next_moves(x):
            if 1 <= nx <= L and dist[nx] == -1:
                dist[nx] = dist[x] + 1
                q.append(nx)
    
    return -1