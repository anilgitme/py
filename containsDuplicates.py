        
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        noDups = {}
        for num in nums:
            if num not in noDups:
                noDups[num] = 1
            else:
                return True
        return False