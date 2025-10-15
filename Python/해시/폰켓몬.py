def solution(nums):
    kind = set(nums)
    
    # 내부 종류만큼 고르거나, 만들 수 있는 최대값으로 만들거나
    return min(len(kind), len(nums) // 2)