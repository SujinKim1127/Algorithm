class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        n = len(nums)

        for i in range(n-2):
            seen = set()
            target = -nums[i]

            for j in range(i + 1, n):
                need = target - nums[j]
                if need in seen:
                    res.add((nums[i], need, nums[j]))
                seen.add(nums[j])
        return [list(t) for t in res]