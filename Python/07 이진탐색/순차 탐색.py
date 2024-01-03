def sequential_search(n, target, array):
    # 각 원소 하나씩 확인하며
    for i in range(n):
        # 현재의 원소가 찾고자 하는 원소와 동일할 경우
        if array[i] == target:
            return i + 1    # 현재 위치 반환 (인덱스는 0부터 시작하니까 1 더해주기)

print("생성할 원소 개수를 입력한 다음 한칸 띄고 찾을 문자열을 입력하세요")
input_data = input().split()
n = int(input_data[0])  #원소 개수
target = input_data[1]  # 찾고자 하는 문자열

print("앞서 적은 원소 개수만큼 문자열을 입력하세요. 구분은 띄어쓰기 한칸으로")
array = input().split()

# 순차탐색 수행 결과 
print(sequential_search(n, target, array))