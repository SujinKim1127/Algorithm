# 1 2 3 4

# 1 - 2명 (2,3,4 중 하나)
# 2 - 1명 (3, 4 중 하나)
# 3 - 1명 (4)
# 4 - 0명

# 1 - 6명 (2, 3, 4, 5, 6, 7)
# 2 - 1명 (3, 4, 5, 6, 7)
# 3 - 1명 (4, 5, 6, 7)
# 4 - 1명 (5, 6, 7)
# 5 - 2명 (6, 7)
# 6 - 0명 ( )
# 7 - 0명

# 0 0 0 0 0 0 1

# 0 2 0 0 0 0 1

# 0 2 3 0 0 0 1

# 0 2 3 4 0 0 1

# 0 2 3 4 0 5 1

# 6 2 3 4 0 5 1

# 6 2 3 4 7 5 1

import sys
input = sys.stdin.readline

n = int(input())

mem = list(map(int, input().split()))

answer = [0] * n

for i in range(n):
  cnt = 0
  for j in range(n):
    if answer[j] == 0:
      cnt += 1
    if cnt == mem[i] + 1:
      answer[j] = i + 1
      break

print(*answer)