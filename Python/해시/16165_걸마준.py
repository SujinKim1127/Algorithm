import sys
input = sys.stdin.readline

n, m = map(int, input().split())
hash = {}
for _ in range(n):
    group = input().rstrip()
    num = int(input())
    for _ in range(num):
        member_name = input().rstrip()
        hash[member_name] = group  # 멤버에다가 그룹 명을 등록

def printbygroup(group_name):
    group_list = []

    for key, value in hash.items():
        if value == group_name:
            group_list.append(key)

    for ans in sorted(group_list): print(ans)


for _ in range(m):
    name = input().rstrip()
    num = int(input())

    if num == 0: printbygroup(name)
    else: print(hash[name])