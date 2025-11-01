class Solution:
    def climbStairs(self, n: int) -> int:
        if n > 2:
            dp = [0] * (n+1)
            dp[1] = 1
            dp[2] = 2

            for x in range(3,n+1):
                dp[x] = dp[x-1] + dp[x-2]
                print(dp[x])
        
        else: 
            if n == 1: return 1
            else: return 2

        return dp[n]