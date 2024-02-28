import sys
input = sys.stdin.readline

test = int(input())
for _ in range(test):
    n, m = map(int, input().split())
    queue = list(map(int, input().split()))
    cnt = 0     # 출력값
    while queue:
        print('--------', cnt, queue, m)
        big = max(queue)    # 가장 먼저 배출되는 현재 최대값
        front = queue.pop(0)
        m -= 1

        if big == front: # 뽑은 숫자가 가장 큰 숫자 일때
            cnt += 1    # 하나가 배출되었으니까
            if m < 0:   # 내 차례
                print(cnt)
                break
        else:
            queue.append(front)
            # 맨 뒤로 이동하기
            if m < 0: m = len(queue) - 1

