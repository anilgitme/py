class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        values = {}
        duplicates = []
        if len(nums) <= 1:
            return []
        
        for num in nums:
            if num not in values:
                values[num] = 1
            else:
                duplicates.append(num)
        return duplicates



A = Solution()
print(A.findDuplicates([4,3,2,7,8,2,3,1]))
print(A.findDuplicates([0]))
print(A.findDuplicates([]))
print(A.findDuplicates([1,2,3,4,5]))
print(A.findDuplicates([-2,-2,-3,-4,-4,-10]))