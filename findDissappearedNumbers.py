class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        nums.sort()

        prev = 0
        nums.append(len(nums)+1)

        res = []

        for num in nums:
            if num - prev > 1:
                res.extend(range(prev + 1, num))
            prev = num
        return res

A = Solution()

print(A.findDisappearedNumbers([4,3,2,7,8,2,3,1]))
print(A.findDisappearedNumbers([1,1]))
print(A.findDisappearedNumbers([]))
print(A.findDisappearedNumbers([0,2,4,6]))  