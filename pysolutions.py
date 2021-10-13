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

#--------------------------------------------

"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:

Input: nums = []
Output: []
Example 3:

Input: nums = [0]
Output: []
"""

def threeSum(nums):
    """
    [-1,0,1,2,-1,-4]
    sort the list
    use 2 points 1 left and 1 right increment each side as a triplet is found
    
    if their is less than 3 numbers in the array then res should be []
    all nums = 0 should return [0, 0 ,0]
    add 3 numbers in the array to see if the sum adds up to 0
    use a dictionary to store the results return the keys at the end
    """
    def threeSum(nums):
        if len(nums) < 3:
            return []
    
        if(all(num == 0 for num in nums)):
            return [[0, 0, 0]]
    
    size = len(nums)
    triplets = {}
    nums = sorted(nums)
    for index, value in enumerate(nums):
        left = index + 1
        right = size - 1
        
        while left < right:
            total = value + nums[left] + nums[right]
            if total == 0:
                current = (value, + nums[left], nums[right])
                if current not in triplets:
                    triplets[current] = True
                right = right - 1
            elif total < 0:
                left = left + 1
            else:
                right = right - 1
    return list(triplets.keys())



# ---------------------------------------------------

"""
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.
"""

def removeDuplicates(nums):
    """
Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]

check the size of the array or 0 or 1 should return the size
make a count variable increment each time an elm dont match the next element 
on the return increment count by 1
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
    """
    size = len(nums)
    count = 0
    if size == 0 or size == 1:
        return size

    for i in range(1 , size):
    # If the current element is equal to the next element, skip
        if nums[i] != nums[count]:
            count += 1
            nums[count] = nums[i]
    return count + 1


    """
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both cases.
"""

def reverseVowels(s):
    """
    Input: s = "hello"
    Output: "holle"
    use 2 points 1 index starting at the front one at the back of the arr
    check if each chr is a vowel if not increment if its at the front decrement if the index is at the back
    """
    vowels = 'aeiou'
    string = list(s)
    i, j = 0, len(s) - 1
    while i < j:
        if string[i].lower() not in vowels:
            i += 1
        elif string[j].lower() not in vowels:
            j -= 1
        else:
            # in case their is a match make a swap
            string[i], string[j] = string[j], string[i]
            j -= 1
            i += 1
    return "".join(string)
    
 
print(reverseVowels('hello'))

# --------------------------------------------------


"""
You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.

Letters are case sensitive, so "a" is considered a different type of stone from "A".
"""

class Soultion:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        """
        Example 1:

        Input: jewels = "aA", stones = "aAAbbbb"
        Output: 3
        Example 2:

        Input: jewels = "z", stones = "ZZ"
        Output: 0
        stones = "AnilGiTME"
        jewels = "AGiT"
        output should be 5
        
        test (numJewelsInStones("AnilGiTME", "AGiT")) ==> 5
        test 2 (numJewelsInStones("AAAAA", "a"))  ===> 0
        test 3 print(numJewelsInStones("", "A"))  ==> 0
        
        could use a loop to check if stone contains  a given jewel character
        hash the given jewel and check if teh str contains that element in the hash increment 
        count if it contains
        """
        
        count = 0
        myJewels = {}
        if len(jewels) == 0:
            return count
        
        for char in jewels:
            myJewels[char] = 1
        for letter in stones:
            if letter in myJewels:
                count += 1
        return count




        # --------------------------------------------------

        """  
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
   
 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
"""
import collections

# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         """
#         Input: nums = [1,1,1,2,2,3], k = 2
#         Output: [1,2]
#         1 and 2 are repeated k times so the output array includes them
#         test 1 nums = []   => []
#         test 2 nums = [2] => [2]
#         test 3 nums = [3,3,3,3,3] => [3]
        
#         algo store the list in a hash
#         loop through the hash and check if that value is repeated k times
#         """
        
#         return [num for num, _ in collections.Counter(nums).most_common(k)] 

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Input: nums = [1,1,1,2,2,3], k = 2
        Output: [1,2]
        1 and 2 are repeated k times so the output array includes them
        test 1 nums = []   => []
        test 2 nums = [2] => [2]
        test 3 nums = [3,3,3,3,3] => [3]
        
        algo store the list in a hash
        loop through the hash and check if that value is repeated k times
        """
        
        return [num for num, _ in collections.Counter(nums).most_common(k)] 

# -------------------------------------------------------------



"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

 

Example 1:

Input: nums = [2,2,1]
Output: 1
Example 2:

Input: nums = [4,1,2,1,2]
Output: 4
""" 

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        none empty array
        test1 nums = [1,1,1,1,1]
        return -1
        
        store all elements in an dictionary
        iterate through the dictionary and return the value that is 1
        """
        store_nums = dict()
        for num in nums:
            if num not in store_nums:
                store_nums[num] = 1
            else:
                store_nums[num] += 1
                
        for key, value in store_nums.items():
            if value == 1:
                return key
        return -1
