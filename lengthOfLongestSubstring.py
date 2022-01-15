class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        j = 0
        ans = 0
        
        for i in range(len(s)):
            while s[i] in chars:
                chars.remove(s[j])
                j += 1
            chars.add(s[i])
            ans = max(ans, i - j + 1)
        return ans
        

A = Solution()
print(A.lengthOfLongestSubstring("pwwkew"))
print(A.lengthOfLongestSubstring("aabcaabcbb"))
print(A.lengthOfLongestSubstring("bbb"))
print(A.lengthOfLongestSubstring(""))
print(A.lengthOfLongestSubstring("zzxxccvv"))