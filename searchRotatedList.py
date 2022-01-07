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



#2


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        
        if not nums:
            return -1
        
        while l <= r:
            mid = (l + r) // 2
            
            if target == nums[mid]:
                return mid
            
            if nums[mid] >= nums[l]: 
                if target >= nums[l] and target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if target > nums[mid] and target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
                
        return -1


obj = Solution()

print(obj.search([[4,5,6,7,0,1,2]], 0))
print(obj.search([[4,5,6,7,-1,-2,-3]], -3))
print(obj.search([[]], 0))
print(obj.search([[1]], -1))