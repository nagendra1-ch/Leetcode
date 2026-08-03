class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)   # Faster lookup
        dp = [False] * (len(s) + 1)
        dp[0] = True               # Empty string is always valid

        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break   # No need to check further once True

        return dp[len(s)]

