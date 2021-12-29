class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        dict_p, dict_w = {}, {}
        s = s.split()
        
        if len(s) != len(pattern):
            return False
        
        for i, word in enumerate(s):
            curPat = pattern[i]
            if word not in dict_w and curPat not in dict_p:
                dict_w[word] = curPat
                dict_p[curPat] = word
            if dict_p.get(curPat) != word or dict_w.get(word) != curPat:
                return False
        return True


A = Solution()  
print(A.wordPattern('abba', "dog mouse cat dog"))
print(A.wordPattern('', "dog cat cat dog"))
print(A.wordPattern('abba', "dog cat cat dog"))
print(A.wordPattern('abba', ""))
print(A.wordPattern('zzz', "z z z"))
print(A.wordPattern('ab', "hello world"))