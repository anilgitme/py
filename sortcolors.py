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