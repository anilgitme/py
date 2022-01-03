import random
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        size = len(nums)
        if size <= 1:
            return nums
        
        pivot_index = random.randint(0, size - 1)
        nums[pivot_index], nums[-1] = nums[-1], nums[pivot_index]
        pivot = nums.pop()
        
        nums_lower = []
        nums_greater = []
        
        for num in nums:
            if num > pivot:
                nums_greater.append(num)
            else:
                nums_lower.append(num)
        return self.sortArray(nums_lower) + [pivot] + self.sortArray(nums_greater)
    
A = Solution()
print(A.sortArray([1,3,0,10,7,20]))
print(A.sortArray([]))
print(A.sortArray([-1]))
print(A.sortArray([-10,0,-5,10,20,1]))
print(A.sortArray([0,0,0]))
print(A.sortArray([1,2,3,4]))