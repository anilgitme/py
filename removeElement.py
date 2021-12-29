class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left = 0
        right = len(nums) - 1
        count = 0
        size = len(nums)
        
        if val not in nums:
            return size
        
        while left < size:
            if nums[left] == val:
                count += 1
                nums[left] = ""
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1
            else:
                left += 1
        return size - count
    
A = Solution()

print(A.removeElement([3,2,2,3], 3))
print(A.removeElement([], 2))
print(A.removeElement([0,1,2,2,3,0,4,2], 2))
print(A.removeElement([2,2,2,2,2,2,2], 2))