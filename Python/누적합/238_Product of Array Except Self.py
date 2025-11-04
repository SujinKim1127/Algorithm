class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        answer = [0] * (n)

        leftPrefix = [nums[0]]

        for i in range(1, n-1):
            leftPrefix.append(leftPrefix[i-1] * nums[i])
            print(i , leftPrefix[i])

        rightProd = 1
        print(leftPrefix, answer)
        for i in range(n - 1, 0, -1):
            answer[i] = leftPrefix[i-1] * rightProd
            print(i, leftPrefix[i-1], nums[i], rightProd)
            rightProd *= nums[i]
        answer[0] = rightProd

        return answer