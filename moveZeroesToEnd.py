class Solution:
    def moveZeroesToEnd(self, nums: List[int]) -> None:
        i = 0
        size = len(nums) - 1
        j = 0
        
        while i <= size:
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1
            else:
                i += 1
        return nums
            

A = Solution()
print(A.moveZeroesToEnd([0,1,0,3,12]))
print(A.moveZeroesToEnd([0,0,1,0,0]))
print(A.moveZeroesToEnd([-1, 0, -2, -3, -4]))
print(A.moveZeroesToEnd([10,100,0,0,1]))
print(A.moveZeroesToEnd([]))
    


#2


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        size = len(nums)
        if size <= 1:
            return nums
        
        i, j = 0, 0
        
        for i in range(size):
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
        return nums
        
A = Solution()
print(A.moveZeroes([0,1,0,3,12]))
print(A.moveZeroes([1,0]))
print(A.moveZeroes([0]))
print(A.moveZeroes([]))
print(A.moveZeroes([-2,0,-1,0,-10]))