def solution(clothes):
    answer = 1
    category = {}
    for name, type in clothes:
        category[type] = category.get(type, 0) + 1
    
    for count in category.values():
        answer *= (count + 1)   # 아예 안입는 경우라서 +1
    
    return answer - 1