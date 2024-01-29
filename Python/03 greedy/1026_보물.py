N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort(reverse=True)

result = 0

for x in range(0, N):
    result += A[x] * B[x]

print(result)