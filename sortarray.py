from typing import List
import random

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        size = len(nums)
        if size <= 1:
            return nums

        pivot_index = random.randint(0, size - 1)
        temp = nums[pivot_index]
        nums[pivot_index] = nums[-1]
        nums[-1] = temp
        pivot = nums.pop()

        greater_nums = []
        lower_nums = []

        for num in nums:
            if num > pivot:
                greater_nums.append(num)
            else:
                lower_nums.append(num)
        
        return self.sortArray(lower_nums) + [pivot] + self.sortArray(greater_nums)

A = Solution()
print(A.sortArray([5,3,6,9,1]))
print(A.sortArray([]))
print(A.sortArray([9]))
print(A.sortArray([0,0,0]))
print(A.sortArray([1,2,3,4]))
print(A.sortArray([4,3,2,1]))



        
