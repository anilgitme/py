class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0 and len(haystack) == 0:
            return 0
        i = 0
        j = len(haystack) - 1
        k = len(needle)
        while i <= j:
            if haystack[i:i + k] == needle:
                return i
                break
            i += 1
        return - 1

A = Solution()
print(A.strStr("hello", "ll"))
print(A.strStr("aaaa", "ba"))
print(A.strStr("", ""))
print(A.strStr("one", "e"))