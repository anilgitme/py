class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x
        
        left = 0
        right = x
        res = 0
        while left < right:
            mid = (left + right) //2
            if mid*mid <= x:
                res = mid
                left = mid + 1
            else:
                right = mid
                
        return res


obj = Solution()
print(obj.mySqrt(4))
print(obj.mySqrt(9))
print(obj.mySqrt(1))
print(obj.mySqrt(10))