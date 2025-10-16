n = int(input())

rope = [int(input()) for _ in range(n)]
rope.sort()

for i in range(n):
    rope[i] *= (n - i)

print(max(rope))