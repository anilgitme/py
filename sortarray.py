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

#2

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        length = len(nums)
        if length <= 1:
            return nums
        
        pivot_index = random.randint(0, length - 1)
        nums[pivot_index], nums[-1] = nums[-1], nums[pivot_index]
        pivot = nums.pop()
        bigNums = []
        smallNums = []
        
        for num in nums:
            if num > pivot:
                bigNums.append(num)
            else:
                smallNums.append(num)    
        return self.sortArray(smallNums) + [pivot] + self.sortArray(bigNums)


A = Solution()  
print(A.sortArray([5,1,1,2,0,0]))
print(A.sortArray([]))
print(A.sortArray([-2,0,-5,-10,1,10]))
print(A.sortArray([1,2,3]))
print(A.sortArray([0]))

        
