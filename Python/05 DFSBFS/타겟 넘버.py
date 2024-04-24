def solution(numbers, target):
    answer = 0
    calculate = [0]
    for num in numbers:
        temp = []
        
        for x in calculate:
            temp.append(x + num)
            temp.append(x - num)
        calculate = temp
    
    for cal in calculate:
        if cal == target:
            answer += 1
    return answer