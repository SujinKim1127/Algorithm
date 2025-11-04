class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            gap = target - nums[i]
            if gap in hashmap:
                return [i, hashmap[gap]]
            
            hashmap[nums[i]] = hashmap.get(nums[i], 0) + i
                        