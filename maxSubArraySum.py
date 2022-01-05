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



#2

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 0:
            return []
        
        curMax = nums[0]
        curSum = 0
        
        for num in nums:
            curSum += num
            if curSum < 0:
                curSum = 0
            if curSum > curMax:
                curMax = curSum
        if curSum == 0 and curMax > curSum:
            return curMax
        elif curSum == 0:
            return max(nums)
        
        return curMax
            
        
A = Solution()
print(A.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(A.maxSubArray([]))
print(A.maxSubArray([-10,-20,5,-40]))
print(A.maxSubArray([-10]))
print(A.maxSubArray([5,4,-1,7,8]))
print(A.maxSubArray([1,1,-2]))