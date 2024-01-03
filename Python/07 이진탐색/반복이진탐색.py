def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2    # 중간점

        # 찾으면 중간점 인덱스 반환
        if array[mid] == target:
            return mid
        # 중간점 값 > 찾으려는 값 : 왼쪽 확인하기
        elif array[mid] > target:
            end = mid - 1
        # 중간점 값 < 찾으려는 값 : 오른쪽 확인
        else:
            start = mid + 1
    return None
    
# n(원소의 개수)와 target(찾으려는 값)을 입력받기
n, target = list(map(int, input().split()))
# 전체 원소 입력받기
array = list(map(int, input().split()))

# 이진 탐색 수행 결과 출력
result = binary_search(array, target, 0, n - 1)
if result == None:
    print("원소가 존재하지 않습니다")
else: 
    print(result + 1)

    