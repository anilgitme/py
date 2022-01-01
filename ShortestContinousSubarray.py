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
print(A.findUnsortedSubarray([5]))
print(A.findUnsortedSubarray([8,7,1,2,8,9,20]))
print(A.findUnsortedSubarray([]))
print(A.findUnsortedSubarray([1,2,3,3,3]))