from collections import deque

n, k = map(int, input().split())

result = []

count = [0] * 100001

def bfs(x):
    queue = deque([x])

    while queue:
        v = queue.popleft()
        # print("count", count)
        # print("VvvvvvvvvvvvV", v)
        if v == k: 
            print(count[v])
            break
        for i in (v-1, v + 1, v * 2):
            if 0<=i<=100000 and count[i] == 0:
                count[i] = count[v] + 1
                queue.append(i)
                # print("queue", queue)
    
    return sum(count)

bfs(n)



# def dfs(x, cnt):
#     cnt += 1
#     small = min(abs(k - (x - 1)), abs(k - (x + 1)), abs(k - (2*x)))
#     if small == 0: 
#         if n == x: cnt = 2
#         result.append(cnt)
#     elif small == abs(k - (x - 1)):
#         dfs(x-1, cnt)
#     elif small == abs(k-(x + 1)):
#         dfs(x+1, cnt)
#     elif small == abs(k - (x * 2)):
#         dfs(x*2, cnt)

# dfs(n, 0)
