array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    for j in range(i, 0, -1):   # i 인덱스부터 1까지 감소하며 반복
        if array[j] < array[j - 1]:
            array[j], array[j - 1] = array[j - 1], array[j]     # 한칸씩 왼쪽으로 이동
        else:   # 자기보다 작은 데이터를 만나면 그 위치에서 멈춤
            break

print(array)