m = int(input())

# 0의 개수
def find0(num):
    count = 0
    while num >= 5:
        count += (num // 5)
        num //= 5 
    return count

start = 1
end = m * 5
res = 0
while start <= end:
    mid = (start + end) // 2
    if find0(mid) >= m:
        end = mid - 1
        res = mid
    else: start = mid + 1

if(m == find0(res)): print(res)
else: print(-1)