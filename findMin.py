class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        if not nums:
            return nums
        
        while left < right:
            mid = left + (right - left) // 2
            
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]        
        
        
obj = Solution()
print(obj.findMin([3,4,5,1,2]))
print(obj.findMin([]))
print(obj.findMin([0]))
print(obj.findMin([1,-1]))
print(obj.findMin([1,2,3,4]))
print(obj.findMin([4,3,2,1]))