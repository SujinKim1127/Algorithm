t = int(input())
for _ in range(t):
    n = int(input())
    grade = []
    for _ in range(n):
        grade.append(list(map(int, input().split())))

    grade.sort(key = lambda x: x[0])
    cnt = 1
    min = grade[0][1]
    for i in range(1, n):
        if min > grade[i][1]:
            cnt += 1
            min = grade[i][1]

    print(cnt)
