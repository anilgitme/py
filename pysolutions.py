"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""
def twoSum(nums, target):
    """
    use 2 loops 
    compare the 2 indicies with the target
    if its a match return the first occurance of the indicies 
    
    constrints: only one solution
    [2,7,11,15] target: 9
    should return (0, 1)  
    """
    
    for i in range(0, len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
            
# output ==> [0, 1]

# print(twoSum([0], 0))
# ==>None

#------------------------------------

"""
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.

Notice that you may not slant the container.

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1
Example 3:

Input: height = [4,3,2,1,4]
Output: 16
Example 4:

Input: height = [1,2,1]
Output: 2
 

Constraints:

n == height.length
2 <= n <= 105
0 <= height[i] <= 104
"""

def maxArea(height):
    """
tranverse the array with 2 loops
first loop starts at the index 0 (i)
second loop starts at index (i + 1) (j)
update the max area of the given list on each iteration until the loops finishes
    """
    area = 0
    for i in range(0, len(height)):
        print(height[i])
        for j in range(i + 1, len(height)):
            print(height[j])
            area = max(area, min(height[j], height[i]) * (j - i))
            # print(area)
            # print(j - i)
    return area

#------------------------------------------------------

"""
Given a string s, find the length of the longest substring without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Input: s = "pwwkew"
             i
              j
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

def lengthOfLongestSubstring(str):
    """
    use 2 points in the string (i, j)
    str = 'a b c a b c b b'
           i                     i remains constant 
           j                     j is incremented by 1 each iteration
           have a start point and max_len starting at (0)
           if a duplicate char is found update the start point 
           dict = {a: 2, b: 4, c: 2,}
    """
    if len(str) == 0:
        return 0
    
    dict = {}
    max_len = start = 0
    
    for i in range(len(str)):
        if str[i] in dict and start <= dict[str[i]]:
            start = dict[str[i]] + 1
        else:
            max_len = max(max_len, i - start + 1)
        dict[str[i]] = i
    return max_len

#---------------------------------------------

"""
Write a function that reverses a string. The input string is given as an array of characters s.

 

Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
 

Constraints:

1 <= s.length <= 105
s[i] is a printable ascii character.
 

Follow up: Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.
"""
def reverseString(s):
    """
    Do not return anything, modify s in-place instead.
    use 2 points of the string 1 right 1 left
    ["h","e","l","l","o"]
     l                 r
     reassign left as right an right as left
    """
    left, right = 0, len(s) -1
    while left < right:
        s[left], s[right] =  s[right], s[left]
        left += 1
        right -= 1
