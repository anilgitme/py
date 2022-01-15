class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        res = 0
        
        while left < right:
            length = (right - left)
            width = min(height[left], height[right])
            area = length * width
            res = max(res, area)
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return res

obj = Solution()
print(obj.maxArea([1,8,6,2,5,4,8,3,7]))
print(obj.maxArea([1,1]))
print(obj.maxArea([10,1,1]))
print(obj.maxArea([]))