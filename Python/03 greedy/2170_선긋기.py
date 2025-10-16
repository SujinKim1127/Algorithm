import sys
input = sys.stdin.readline

n = int(input())

lines = []

for _ in range(n):
    x, y = map(int, input().split())
    lines.append((x, y))

lines.sort()

start = lines[0][0]
end = lines[0][1]

total = 0

for x, y in lines[1:]:
    if end >= x:
        end = max(end, y) 
    else:
        total += end - start
        start, end = x, y

print(total + end - start)