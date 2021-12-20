class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        mapp = dict.fromkeys(dictionary)
        
        s = sentence.split()
        
        for i, value in enumerate(s):
            j = 1
            
            while j < len(value):
                substr = value[:j]
                if substr in mapp:
                    s[i] = substr
                    break
                j += 1
        return ' '.join(s)
    
    
A = Solution()
print(A.replaceWords(["cat","bat","rat"], "the cattle was rattled by the battery"))
print(A.replaceWords(['san','tow'], "santa is coming to town"))
print(A.replaceWords(['lad'], "the ladder is too high"))