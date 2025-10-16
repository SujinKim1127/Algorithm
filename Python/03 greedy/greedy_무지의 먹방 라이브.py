
food_times = [8, 6, 4, 5]
k=20


# def solution(food_times, k):
#     if(sum(food_times) < k): return -1
#     answer = 0
#     cnt = 0
#     for i in range(k):
#         pres = i % len(food_times)
#         if(food_times[pres] != 0):
#              food_times[pres] -= 1
#         elif(food_times[pres] == 0):
#             pres = (i + 1) % len(food_times)
#             food_times[pres] -= 1
#         print("food", food_times)
#         answer = (pres+1)%len(food_times) + 1
#     return answer + 1



### answer ####
import heapq

def solution(food_times, k):
    # 전체 음식을 먹는 시간보다 k가 크거나 같다면 -1
    if(sum(food_times)) <= k:
        return -1
    
    # 시간이 작은 음식부터 빼야 하므로 우선순위 큐 이용
    q = []
    for i in range(len(food_times)):
        # (음식시간, 음식번호) 형태로 우선순위 큐에 삽입
        heapq.heappush(q, (food_times[i], i + 1))
    print("q", q)
    
    sum_value = 0  # 먹기 위해 사용한 시간
    previous = 0  # 직전에 다 먹은 음식 시간
    length = len(food_times)  # 남은 음식 개수

    # sum_values + (현재의 음식 시간 - 이전 음식 시간) * 현재 음식 개수와 k 비교
    while sum_value + ((q[0][0] - previous) * length) <= k :
        now = heapq.heappop(q)[0]
        sum_value += (now - previous) * length
        length -= 1     # 다 먹은 음식 빼기
        previous = now  # 이전 음식 시간 재설정
        print("now", now)
        print("pre", previous)
        print(q)
    
    # 남은 음식 중에서 몇 번째 음식인지 확인하여 출력
    result = sorted(q, key =lambda x: x[1])     # 음식의 번호 기준으로 정렬
    return result[(k-sum_value) % length][1]


print(solution(food_times, k))
