# 이진탐색

## 순차탐색

- 리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 차례대로 확인하는 방법
- 정렬되지 않은 리스트에서 데이터를 찾아야 할때 사용
- 장점: 리스트 내에 데이터가 아무리 많아도 시간만 충분하면 원하는 데이터를 항상 찾을 수 있다
- 리스트에 특정 값의 원소 있는지 체크할 때, 특정한 값을 가지는 원소의 개수를 count 할때

```python
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

# 생성할 원소 개수를 입력한 다음 한칸 띄고 찾을 문자열을 입력하세요
# 5 dongbin
# 앞서 적은 원소 개수만큼 문자열을 입력하세요. 구분은 띄어쓰기 한칸으로
# hanul dongbin taiel joongu sagnwook
# 2
```

- 데이터의 개수가 N개 일때 최대 N번의 비교 연산이 필요 ⇒ 최악의 시간복잡도: $O(N)$

## 이진 탐색: 반으로 쪼개면서 탐색하기

- 배열 내부의 데이터가 정렬되어 있어야만 사용 가능
- 내부 데이터가 이미 정렬되어 있다면 빠르게 탐색 가능
- 탐색 범위를 절반씩 좁혀가며 데이터 탐색
- 위치 변수 3개(시작점, 끝점, 중간점) 사용
- 찾으려는 데이터와 중간점 위치에 있는 데이터를 반복적으로 비교해서 원하는 데이터 찾기

![image](https://github.com/SujinKim1127/Algorithm/assets/58413633/49f1b569-c276-48b4-b814-0dc84ca85b81)

- 한번 확인할 때마다 확인하는 원소의 개수 감소 ⇒ 시간복잡도: $O(logN)$

### 재귀함수로 이진탐색 구현하기

```python
def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2    # 중간점

    # 찾으면 중간점 인덱스 반환
    if array[mid] == target:
        return mid
    # 중간점 값 > 찾으려는 값 : 왼쪽 확인하기
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    # 중간점 값 < 찾으려는 값 : 오른쪽 확인
    else:
        return binary_search(array, target, mid + 1, end)
    
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

----------------------
10 7
1 3 5 7 9 11 13 15 17 19
4

10 7
1 3 5 6 9 11 13 15 17 19
원소가 존재하지 않습니다
```

### 반복문으로 이진탐색 구현하기

```python
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

----------------------
10 7
1 3 5 7 9 11 13 15 17 19
4

10 7
1 3 5 6 9 11 13 15 17 19
원소가 존재하지 않습니다
```

---

### 코딩테스트에서의 이진탐색

- 이진 탐색은 코딩테스트 단골 문제니까 외우자!
- 탐색 범위가 2000만을 넘어가면 이진 탐색으로 문제 접근하기
- 처리해야할 데이터의 개수나 값이 1000만 단위 이상이면 $O(logN)$ 속도 필요

## 트리 자료구조

- 노드와 노드의 연결로 표현
- 그래프 자료구조 중 하나
- 데이터베이스 시스템이나 파일 시스템과 같은 곳에서 많은 양의 데이터를 관리하기 위한 목적으로 사용

<aside>
💡 주요 특징
- 트리는 부모 노드와 자식 노드의 관계로 표현된다
- 트리는 최상단 노드를 루트 노드라고 한다
- 트리의 최하단 노드를 단말 노드라고 한다
- 트리에서 일부를 떼어내도 트리 구조이며 이를 서브 트리라 한다
- 트리는 파일 시스템과 같이 계층적이고 정렬된 데이터를 다루기에 적합하다

</aside>

## 이진 탐색 트리

- 트리 자료구조 중에서 가장 간단한 형태
- 이진 탐색이 동작할 수 있도록 고안된, 효율적인 탐색이 가능한 자료구조

<aside>
💡 주요 특징
- 부모 노드보다 왼쪽 자식 노드가 작다
- 부모 노드보다 오른쪽 자식노드가 크다

</aside>

> 왼쪽 자식 노드 < 부모 노드 < 오른쪽 자식 노드
> 

![image](https://github.com/SujinKim1127/Algorithm/assets/58413633/d549a0e6-386d-4982-a30c-2bb7bb588369)

공식에 따라 루트 노드부터 왼쪽 자식 노드 혹은 오른쪽 자식 노드로 이동하며 반복적으로 방문

### 빠르게 입력 받기

- 데이터 개수가 1000만개를 넘어가거나 탐색 범위 크기가 1000억 이상 ⇒ 이진 탐색 알고리즘

⇒ 입력 데이터의 개수가 많은 문제에 input() 사용하면 동작속도가 느려진다

sys 라이브러리 readline() 함수를 이용하자!!!

```python
import sys
# 하나의 문자열 데이터 입력받기
input_data = sys.stdin.readline().rstrip()

# 입력받은 문자열 그대로 출력
print(input_data)
```

sys 라이브러리 사용시 주의 사항

→ 한 줄 입력받고 나서 rstrip() 함수 꼭 호출하기

readline() 사용하면 엔터가 줄바꿈 기호로 입력되기 때문
