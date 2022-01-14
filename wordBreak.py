class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        size = len(s)
        dp = [False] * (size + 1)
        dp[0] = True 
        
        for i in range(1, size + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict: 
                    dp[i] = True
                    break
        return dp[size]

    
A = Solution()
print(A.wordBreak("catsandog", ["cats","dog","sand","and","cat"]))
print(A.wordBreak("sandbox", ["sand","box"]))
print(A.wordBreak("code", []))
print(A.wordBreak("l", ["lll"]))