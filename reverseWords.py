class Solution:
    def reverseWords(self, s: str) -> str:
        if len(s) <= 1:
            return s
        
        s = s.split() 
        j = len(s) - 1

        for i in range(j):
            if i >= j:
                break
            s[i], s[j] = s[j], s[i]
            j -= 1
        return ' '.join(s)



obj = Solution()
print(obj.reverseWords("blue is sky the"))
print(obj.reverseWords("abc"))
print(obj.reverseWords(""))
print(obj.reverseWords("Word word"))
print(obj.reverseWords("many       spaces"))




