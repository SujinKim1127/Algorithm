from collections import deque 
t = int(input())


def bfs():
    q = deque()
    q.append((house_x, house_y))
    while q:
        x, y = q.popleft()
        # 락페 가기 가능
        if abs(x-rock_x) + abs(y-rock_y) <= 1000:
            print("happy")
            return
        for i in range(n):
            if not visited[i]:  # 방문 안한 편의점
                new_x, new_y = store[i]
                if abs(x-new_x) + abs(y - new_y) <= 1000:   # 편의점까지 가는거 가능하면
                    visited[i] = 1
                    q.append((new_x, new_y))
    print("sad")
    return



for i in range(t):
    n = int(input())        
    house_x, house_y = map(int, input().split())
    store = []
    for _ in range(n):
        store.append(list(map(int, input().split())))
    rock_x, rock_y = map(int, input().split())
    visited = [0 for _ in range(n+1)]
    bfs()