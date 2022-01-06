# class Solution:
#     def wordPattern(self, pattern: str, s: str) -> bool:
#         dict_p, dict_w = {}, {}
#         s = s.split()
        
#         if len(s) != len(pattern):
#             return False
        
#         for i, word in enumerate(s):
#             curPat = pattern[i]
#             if word not in dict_w and curPat not in dict_p:
#                 dict_w[word] = curPat
#                 dict_p[curPat] = word
#             if dict_p.get(curPat) != word or dict_w.get(word) != curPat:
#                 return False
#         return True


# A = Solution()  
# print(A.wordPattern('abba', "dog mouse cat dog"))
# print(A.wordPattern('', "dog cat cat dog"))
# print(A.wordPattern('abba', "dog cat cat dog"))
# print(A.wordPattern('abba', ""))
# print(A.wordPattern('zzz', "z z z"))
# print(A.wordPattern('ab', "hello world"))



#2

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words, patterns = {}, {}
        
        s = s.split()
        if len(s) != len(pattern):
            return False
        elif len(s) == 0 and len(pattern) == 0:
            return None
        
        for i, word in enumerate(s):
            curPattern = pattern[i]
            
            if curPattern not in patterns and word not in words:
                patterns[curPattern] = word
                words[word] = curPattern
            if words.get(word) != curPattern or patterns.get(curPattern) != word:
                return False
        return True
        
obj = Solution()
print(obj.wordPattern("abba", "dog cat cat dog"))
print(obj.wordPattern("a", "should be false"))
print(obj.wordPattern("112", "rat rat bat"))
print(obj.wordPattern("", ""))
print(obj.wordPattern("1", "one"))