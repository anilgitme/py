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
    