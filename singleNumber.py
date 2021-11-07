from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        store_nums = {}
        for num in nums:
            if num not in store_nums:
                store_nums[num] = 1
            else:
                store_nums[num] += 1
                
        for key, value in store_nums.items():
            if value == 1:
                return key
        return -1

A = Solution()
print(A.singleNumber([[4,1,2,1,2]]))
