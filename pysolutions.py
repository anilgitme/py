
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




def reverseVowels(s):
    """
    Input: s = "hello"
    Output: "holle"
    use 2 points 1 index starting at the front one at the back of the arr
    check if each chr is a vowel if not increment if its at the front..decrement if the index is at the back
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



class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import collections
        """
        Input: nums = [1,1,1,2,2,3], k = 2
        Output: [1,2]
        1 and 2 are repeated k times so the output array includes them
        test 1 nums = []   => []
        test 2 nums = [2] => [2]
        test 3 nums = [3,3,3,3,3] => [3]
        
        """
        
        return [num for num, _ in collections.Counter(nums).most_common(k)] 




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


# ---------------------------------------------------------
        

 
    
class Solution:
    # """
    # get the sum on n store the result in a set/hash
    # check if the same number is in the hash if it is 
    # we are in a endless loop return false if the squared sum in 1
    # return True
    # """
    def isHappy(self, n: int) -> bool:
        visited = {n}
        while True:
            n = sum([int(num) ** 2 for num in str(n)])
            
            if n == 1:
                return True
            if n in visited:
                return False
            visited.add(n)
            print(visited)
        return False





class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Input: temperatures = [73,74,75,71,69,72,76,73]
        #                 i
        #                    j
        #                 0  1  
        #                  1   1  4  2 1  1  0  + 0
        #                  0 - 1 = 1
        #                  get the day by subtracting i and j
        days = [0] * len(temperatures)
        # initiliat the length of the result array to all 0s
        
        for i in range(0, len(temperatures)):
            
            for j in range(i + 1, len(temperatures)):
                if temperatures[i] < temperatures[j]:
                    days[i] = j - i
                    # assign the current index of i in my result array
                    break

        return days





class Solution:
    def frequencySort(self, s: str) -> str:
        letters = {}
        string = ""
        for char in s:
            if char not in letters:
                letters[char] = 1
            else:
                letters[char] += 1
        # print(letters)        
        rev_dict = sorted(letters.items(), key = lambda item: item[1], reverse=True)
        # print(rev_dict)
        for key, value in rev_dict:
            string += key * value
        return string


