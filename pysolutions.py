
def twoSum(nums, target):
    for i in range(0, len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
            



def maxArea(height):
    area = 0
    for i in range(0, len(height)):
        print(height[i])
        for j in range(i + 1, len(height)):
            print(height[j])
            area = max(area, min(height[j], height[i]) * (j - i))  
    return area

#------------------------------------------------------




def lengthOfLongestSubstring(str):
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


