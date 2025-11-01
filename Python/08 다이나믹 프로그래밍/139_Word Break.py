class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordset = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(len(s)):
            if dp[i]:
                for j in range(i+1, len(s) + 1):
                    if s[i:j] in wordset:
                        dp[j] = True

        return dp[-1]