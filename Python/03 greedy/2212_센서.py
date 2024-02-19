import sys
input = sys.stdin.readline

N = int(input())
K = int(input())
senser = list(map(int, input().split()))
senser.sort()

if K >= N:
    print(0)
    sys.exit()

gap = []
K -= 1
for x in range(0, N-1):
    gap.append(senser[x+1] - senser[x])
gap.sort()
while K > 0:
    gap.pop()
    K -= 1

print(sum(gap))