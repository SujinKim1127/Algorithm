import sys
input = sys.stdin.readline

n = int(input())
arr = sorted(list(map(int, input().split())))

total = 0
curr = 0
for num in arr:
    curr += num
    total += curr

print(total)