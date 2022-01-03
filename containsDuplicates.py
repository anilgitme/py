        
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        noDups = {}
        for num in nums:
            if num not in noDups:
                noDups[num] = 1
            else:
                return True
        return False

# brute force

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool: 
        size = len(nums)
        if size <= 1:
            return False
        
        for i in range(0, size):
            for j in range(i + 1, size):
                if nums[i] == nums[j]:
                    return True
        return False
        
        
        
A = Solution()
print(A.containsDuplicate([3,0,1,4,1,5]))
print(A.containsDuplicate([0,1,2,3,4,4]))
print(A.containsDuplicate([0,1,2,3,4]))
print(A.containsDuplicate([-6,5,6,1,8,-3,0]))
print(A.containsDuplicate([]))
print(A.containsDuplicate([-1]))