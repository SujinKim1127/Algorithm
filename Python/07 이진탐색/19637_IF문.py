import sys
input = sys.stdin.readline

n, m = map(int, input().split())
chingho = [input().split() for _ in range(n)]
chingho.sort(key=lambda x:int(x[1]))

arr = [int(input().rstrip()) for _ in range(m)]

for x in arr:
    right = n
    left = 0
    result = 0
    while left <= right:
        mid = (left + right) // 2
        if int(chingho[mid][1]) >= x:
            result = mid
            right = mid - 1
        else: 
            left = mid + 1
    print(chingho[result][0])