class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        right = len(nums) - 1
        left = 0
        if len(nums) == 1:
            return [nums[0] * nums[0]]
        elif len(nums) == 0:
            return []
        squares = []
        
        while left <= right:
            numLeft = nums[left] * nums[left]
            numRight = nums[right] * nums[right]
            
            if numLeft > numRight:
                squares.insert(0, numLeft)
                left += 1
            else:
                squares.insert(0, numRight)
                right -= 1
        return squares
        

               
A = Solution()
print(A.sortedSquares([]))
print(A.sortedSquares([10]))
print(A.sortedSquares([-4,-1,0,3,10]))
print(A.sortedSquares([-12,-8,-1,0,5]))
print(A.sortedSquares([1,1,2,2]))