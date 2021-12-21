class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return nums
        
        curMax = nums[0]
        curSum = 0
        if len(nums) == 1:
            return curMax
        
        
        for num in nums:
            curSum += num
            if curSum < 0:
                curSum = 0
            if curSum > curMax:
                curMax = curSum
        if curMax == 0:
            return max(nums)
        
        return curMax        
                
        

A = Solution()
print(A.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(A.maxSubArray([-2,-1]))
print(A.maxSubArray([-2]))
print(A.maxSubArray([]))