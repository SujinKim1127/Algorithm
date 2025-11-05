class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        max_reach = 0
        for i, num in enumerate(nums):
            # 도달하지 못함
            if i > max_reach: return False
            
            if num > 0:
                max_reach = max(max_reach, i + num)

            if max_reach >= n - 1: return True
            
        return False