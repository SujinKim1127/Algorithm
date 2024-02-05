import heapq
import sys
input = sys.stdin.readline

N = int(input())
data = []
for _ in range(N):
    data.append(list(map(int, input().split())))

data.sort()

room = []
heapq.heappush(room, data[0][1])

for x in range(1, N):
    if room[0] > data[x][0]:
        heapq.heappush(room, data[x][1])
    else:
        heapq.heappop(room)
        heapq.heappush(room, data[x][1])

print(len(room))