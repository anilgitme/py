class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        
        if not numbers:
            return -1
        
        while left <= right:
            sumNum = numbers[left] + numbers[right]
            
            if sumNum == target:
                return [left + 1, right + 1]
            
            if target > sumNum:
                left += 1
            else:
                right -= 1
        return -1
        
A = Solution()
print(A.twoSum([2,7,11,15], 9))
print(A.twoSum([], 0))
print(A.twoSum([-4,-3,-2,-1,0,1,2], -6))
print(A.twoSum([-1,0], -1))
print(A.twoSum([3,4,8,7,9], 9))