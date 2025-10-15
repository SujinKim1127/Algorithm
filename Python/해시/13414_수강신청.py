import sys

input = sys.stdin.readline

k, l = map(int, input().split())
hashmap = {}

for _ in range(l):
    number = input().strip()
    if number in hashmap:
        del hashmap[number]     # 기존 위치 제거
    hashmap[number] = True

cnt = 0
out = []

for sid in hashmap.keys():
    out.append(sid)
    cnt += 1
    if cnt == k: break

sys.stdout.write("\n".join(out) + ("\n" if out else ""))

# for item in reversed(hashmap):
#     if item not in seen:
#         seen.add(item)
#         result.append(item)
# hashmap = list(reversed(result))

# for i in range(k):
#     print(hashmap[i])