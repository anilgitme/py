class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:       
        seen = {0:1}
        count = 0
        curSum = 0
        if len(nums) == 0:
            return nums
        
        for num in nums:
            curSum += num
            diff = curSum - k
            if diff in seen:
                count += seen[diff]
            if curSum not in seen:
                seen[curSum] = 1
            else:
                seen[curSum] += 1
        return count
        
A = Solution()  
print(A.subarraySum([1,1,1], 2))
print(A.subarraySum([], 0))
print(A.subarraySum([-1,-2,-3,-4], -1))
print(A.subarraySum([5,5,5,5], 5)) 


#2

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        seen = {0:1}
        cur_Sum = 0
        
        if not nums:
            return nums
        
        for num in nums:
            cur_Sum += num
            
            diff = cur_Sum - k
            
            if diff in seen:
                count += seen[diff]
                
            if cur_Sum not in seen:
                seen[cur_Sum] = 1
            else:
                seen[cur_Sum] += 1
        return count


obj = Solution()
print(obj.subarraySum([1,1,1], 2))
print(obj.subarraySum([1], 1))
print(obj.subarraySum([], 2))
print(obj.subarraySum([1,1,1], 1))
print(obj.subarraySum([0,2,5,7], 0))