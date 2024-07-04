class Solution(object):
    def countBits(self, n):
        dp = [0] * (n+1)
        offset = 1

        for i in range(1,n+1):
            if offset * 2 == i:    # 2 4 8 16에만 if문 들어옴
                offset = i
            print(offset, i - offset, dp[i-offset])
            dp[i] = 1 + dp[i-offset]

        return dp