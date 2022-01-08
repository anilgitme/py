class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1
        res = [-1, -1]
        if not nums:
            return res
        
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                if nums[left] == target and nums[right] == target:
                    res = [left, right]
                    break
                if nums[left] < target:
                    left += 1
                    
                elif nums[right] > target:
                    right -= 1
        return res
        
A = Solution()
print(A.searchRange([5,7,7,8,8,10],8))
print(A.searchRange([],0))
print(A.searchRange([1],1))
print(A.searchRange([-2,-2,0,0,5,5,6],-2))
print(A.searchRange([0,0,0,0],0))