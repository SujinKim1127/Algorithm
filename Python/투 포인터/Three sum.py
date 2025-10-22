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
    
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # res = set()
        nums.sort()
        n = len(nums)
        res = []

        for i in range(n-2):
            # seen = set()
            # target = -nums[i]

            # 중복 i 건너뛰기
            if i > 0 and nums[i] == nums[i - 1]: continue

            l, r = i + 1, n - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    # 중복값 스킵
                    while l < r and nums[l] == nums[l + 1]: l += 1
                    while l < r and nums[r] == nums[r - 1]: r -= 1

                    l += 1
                    r -= 1
                elif s < 0: l += 1
                else: r -= 1
        
        return res
            # for j in range(i + 1, n):
            #     need = target - nums[j]
            #     if need in seen:
            #         res.add((nums[i], need, nums[j]))
            #     seen.add(nums[j])
        # return [list(t) for t in res]