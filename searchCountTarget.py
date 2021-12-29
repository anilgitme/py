class Solution:
    def searchCountTarget(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1
        
        if len(nums) == 0:
            return 0
        elif len(nums) == 1 and target == nums[0]:
            return 1
        
        mid = (left + right) // 2
        
        while left <= right:
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                if nums[left] == target and nums[right] == target:
                    return right - left + 1
                    break
                if nums[left] < target:
                    left += 1
                    
                elif nums[right] > target:
                    right -= 1
            mid = (left + right) // 2
        return 0

A = Solution()   
print(A.searchCountTarget([4, 4, 8, 8, 8, 15, 16, 23, 23, 42], 8))
print(A.searchCountTarget([3,5,6,9], 7))
print(A.searchCountTarget([], 8))
print(A.searchCountTarget([8], 8))
print(A.searchCountTarget([5,5,5,5,5,5], 5))