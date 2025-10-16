n = int(input())

meeting = []

for _ in range(n):
    start, end = map(int, input().split())
    meeting.append((start, end))

meeting.sort(key=lambda x:(x[1], x[0]))

last = 0
count = 0

for s, e in meeting:
    if s >= last:
        count += 1
        last = e

print(count)