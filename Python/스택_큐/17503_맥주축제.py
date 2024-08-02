import heapq
import sys
input = sys.stdin.readline

count, total, kind= map(int, input().split())

bear = []
heap = []
heapq.heapify(heap)

for _ in range(kind):
    prefer, level = map(int, input().split())
    bear.append((prefer, level))

# 레벨 순으로 오름차순
bear.sort(key=lambda x : (x[1], x[0]))  

find = False
now, sum = 0, 0

for i in range(kind):
    heapq.heappush(heap, bear[i][0])
    sum += bear[i][0]
    now = bear[i][1]
    if len(heap) == count:
        if sum >= total:
            find = True
            print(now)
            break
        else:
            sum -= heapq.heappop(heap)

if not find: print(-1)




