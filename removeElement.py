class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        left = 0
        right = len(nums) - 1
        
        while left < len(nums):
            if nums[left] == val:
                nums[left] = ''
                count += 1
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1
            else:
                left += 1
        return len(nums) - count
    
A = Solution()

print(A.removeElement([3,2,2,3], 3))
print(A.removeElement([], 2))
print(A.removeElement([0,1,2,2,3,0,4,2], 2))
print(A.removeElement([2,2,2,2,2,2,2], 2))