class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        if not nums:
            return nums
        
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid + 1
				
        return left
        
A = Solution()
print(A.findPeakElement([1,2,3,1]))
print(A.findPeakElement([1,2,1,3,5,6,4]))
print(A.findPeakElement([3]))
print(A.findPeakElement([]))