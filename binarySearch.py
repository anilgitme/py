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