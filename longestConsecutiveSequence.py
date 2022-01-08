class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums.sort()
        count = 1
        longest_streak = []

        for index, value in enumerate(nums):
            if index + 1 >= len(nums):
                break
            if nums[index + 1] == value + 1:
                count += 1
                longest_streak.append(count)
            else:
                count = 1

        if not longest_streak:
            return count

        return max(longest_streak)

A = Solution()
print(A.longestConsecutive([9,1,4,7,3,-1,0,5,8,-1,6]))
print(A.longestConsecutive([1]))
print(A.longestConsecutive([]))
print(A.longestConsecutive([-3,-2,-1,0]))
print(A.longestConsecutive([1,1,1,1]))