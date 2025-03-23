class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        while (start <= end):
            mid = (start + end) // 2
            price = nums[mid]
            if (price == target): return mid
            if (price > target):
                end = mid - 1
            if(price < target):
                start = mid + 1
        
        if (target < nums[mid]): return mid
        else: return mid + 1