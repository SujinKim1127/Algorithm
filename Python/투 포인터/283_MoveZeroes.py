class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        not_zero = 0
        n = len(nums)
        for i in range(n):
            if nums[i] != 0:
                print(not_zero)
                nums[not_zero] = nums[i]
                not_zero += 1
        
        for i in range(not_zero, n):
            nums[i] = 0