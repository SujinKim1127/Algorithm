n, c = map(int, input().split())
mesg = list(map(int, input().split()))

cnt = {}

for i in mesg:
    if i not in cnt:
        cnt[i]=0
    cnt[i] += 1

# 정렬
cnt=sorted(cnt.items(), key=lambda x: x[1], reverse=True)

# 갯수만큼 반복 출력
for key, value in cnt:
    for i in range(value):
        print(str(key), end=" ")