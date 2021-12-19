class Solution:
    def searchRotatedList(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if target == nums[mid]:
                return mid
            
            if nums[left] <= nums[mid]:
                if target > nums[mid] or target < nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1
                    
            else:
                if target < nums[mid] or target > nums[right]:
                    right = mid - 1
                else:
                    left = mid + 1
        return -1
                
                
    
    
    
A = Solution()    
print(A.searchRotatedList([4,5,6,7,0,1,2], 0))
print(A.searchRotatedList([2], 2)) 
print(A.searchRotatedList([4,5,6,7,0,1,2], 9)) 
print(A.searchRotatedList([], 0)) 
