n, k = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

for _ in range(k):
    A.sort()
    B.sort(reverse=True)
    print("before:", A, B)
    if(A[0] < B[0]): A[0], B[0] = B[0], A[0]
    else: break
    print("after:", A, B)

print(sum(A))





# ------------answer-------------

A.sort()
B.sort(reverse=True)

for i in range(k):
    if A[i] < B[i]:
        A[i], B[i] = B[i], A[i]
    else:
        break