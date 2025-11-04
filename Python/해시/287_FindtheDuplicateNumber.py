class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hashmap = {}
        for num in nums:
            if hashmap.get(num, 0) > 0: return num
            hashmap[num] = hashmap.get(num, 0) + 1