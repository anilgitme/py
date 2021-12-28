class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) == 0 or len(s2) == 0:
            return False

        j  = len(s1)
        curStr = s2[:j]
    
        for i in range(len(s2) - j):
            if sorted(s1) == sorted(curStr):
                return True
            else:
                curStr = curStr[1:j]
                curStr += s2[i+j]
        
        if sorted(s1) == sorted(curStr):
            return True
    
        return False

                
A = Solution()
print(A.checkInclusion("ba","eidbaooo"))
print(A.checkInclusion("abc","bbbca"))
print(A.checkInclusion("azc","dcda"))
print(A.checkInclusion("bc",""))
print(A.checkInclusion("","abc"))