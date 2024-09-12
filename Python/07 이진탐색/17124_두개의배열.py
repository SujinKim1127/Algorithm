import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int, input().split(' '))
    A = list(map(int, input().split(' ')))
    B = list(map(int , input().split(' ')))
    B.sort()
    cnt = 0
    for a in A:
        left = 0
        right = m - 1
        while left < right:
            mid = (left + right) // 2
            if B[mid] <= a:
                left = mid + 1
            else:
                right = mid
        if left == 0:     # a 값이 B 최소값보다도 작은 경우
            print("left == 0")
            print(a, B[mid], mid)
            cnt += B[mid]
        else: 
            print("left", left)
            print("a, B", a, B[left-1], B[left])
            if a - B[left - 1] > B[left] - a :
                cnt += B[left] 
            else: cnt += B[left - 1]
    print(cnt)

