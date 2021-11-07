from typing import List

class Solution:
    def isHappy(self, n: int) -> bool:
        isSeen = []
        while n != 1:
            isSeen.append(n)
            sumNum = 0
            for num in list(str(n)):
                sumNum += int(num) **2
            n = sumNum
            
            if n == 1:
                return True
            elif n in isSeen:
                return False
        return False
        
       
        
        
A = Solution()
print(A.isHappy(2))
print(A.isHappy(19))