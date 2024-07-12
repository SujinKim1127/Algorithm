import sys

input = sys.stdin.readline

k, n = map(int, input().split())
lan = []
for _ in range(k):
    lan.append(int(input()))

lan.sort()

start = 1         
end = lan[-1]

answer = 0

while start <= end:
    count = 0
    mid = (start + end) // 2    # 중간점

    # 해당 중간값으로 총 몇개 나오는지
    for x in lan:
        count += x // mid
    # 찾으면 중간점 인덱스 반환
    # count 값이 크면? count 값이 작아져야 하므로 mid 값이 커져야 함
    # mid 값이 커지려면? start 값 + 1
    if count >= n:
        start = mid + 1
        answer = mid
    else:
        end = mid - 1


print(answer)