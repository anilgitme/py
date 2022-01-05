class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        
        Input: nums = [2,0,2,1,1,0]
                       j         k
                       i
              Output: [0,0,1,1,2,2]
        """
        j = 0
        i = 0
        k = len(nums)- 1
        
        while i <= k:
            if nums[i] == 0:
                nums[j], nums[i] = nums[i], nums[j]
                i += 1
                j += 1
            elif nums[i] == 1:
                i += 1
            else:
                nums[i], nums[k] = nums[k], nums[i]
                k -= 1


# 2


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        j = 0
        k = len(nums) - 1
        i = 0
        if len(nums) <= 1:
            return nums
        
        while i <= k:
            
            if nums[i] == 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
                i += 1
            elif nums[i] == 2:
                nums[i], nums[k] = nums[k], nums[i]
                k -= 1
            else:
                i += 1
        return nums
        

A = Solution()
print(A.sortColors([2,0,2,1,1,0]))
print(A.sortColors([0,2]))
print(A.sortColors([2,0,1]))
print(A.sortColors([1]))
print(A.sortColors([1,0,0,0,1]))
print(A.sortColors([]))