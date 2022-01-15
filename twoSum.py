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


#2

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        left = 0
        right = len(numbers) - 1
        
        while left <= right:
            total = numbers[left] + numbers[right]
            
            if total == target:
                return [left + 1, right + 1]
            elif target > total:
                left += 1
            else:
                right -= 1
        return -1
        
        
obj = Solution()        
print(obj.twoSum([2,7,11,15],9))
print(obj.twoSum([1],1))
print(obj.twoSum([1,1,1],2))
print(obj.twoSum([-3,-1,0,2,5,7],4))
print(obj.twoSum([],0))