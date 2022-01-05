class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sorted_list = sorted(nums)
        left = 0
        right = len(nums) -1
        
        while left <= right and sorted_list[left] == nums[left]:
            left += 1
            
        while right >= left and sorted_list[right] == nums[right]:
            right -= 1
            
            
        if right > left:
            return right - left + 1
        else:
            return 0
    
A = Solution()
print(A.findUnsortedSubarray([2,6,4,8,10,9,15]))
print(A.findUnsortedSubarray([]))
print(A.findUnsortedSubarray([1,2,3,4]))
print(A.findUnsortedSubarray([1,6,4,5,7]))



#2

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        leftNum = float('-inf')
        rightNum = float('inf')
        rightIdx = 0
        leftIdx = 0
        
        for i in range(len(nums)):
            if nums[i] >= leftNum:
                leftNum = nums[i]
            else:
                rightIdx = i
        

        for j in range(len(nums) -1, -1, -1):
            if nums[j] <= rightNum:
                rightNum = nums[j]
            else:
                leftIdx = j
        if rightIdx > leftIdx:
            return rightIdx - leftIdx + 1
        else:
            return 0
            
            
        
        
A = Solution()
print(A.findUnsortedSubarray([2,6,4,8,10,9,15]))
print(A.findUnsortedSubarray([]))
print(A.findUnsortedSubarray([5]))
print(A.findUnsortedSubarray([0,3,9,8,6,5,10]))
print(A.findUnsortedSubarray([2,2,3,5,4,7,10]))