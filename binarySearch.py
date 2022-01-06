class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        
        while start <= end:
            mid = (start + end) // 2
            
            if nums[mid] == target:
                return mid
            
            if nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        return -1

A = Solution()
print(A.search([-1,0,3,5,9,12],9))
print(A.search([0], 1))
print(A.search([-1,-2], -2))
print(A.search([12,18,99], 99))


#2

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        size = len(nums)
        left = 0
        right = size - 1
        if size == 0:
            return - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return - 1
    
obj = Solution()
print(obj.search([-1,0,3,5,9,12], 9))
print(obj.search([-9,-6,-5,-1,1,5], -5))
print(obj.search([1,8,9,99], 10))
print(obj.search([], 0))
print(obj.search([2], 2))