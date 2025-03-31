from collections import deque
import sys
input = sys.stdin.readline

A, K = map(int, input().split())
c = 0
while A * 2 <= K:
    c += 1 + (K & 1)
    K = K // 2

print(c + K - A)

