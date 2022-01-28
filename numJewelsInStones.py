class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        if not jewels or not stones:
            return 0
        my_dict = {}
        count = 0
        
        for i in range(len(jewels)):
            my_dict[jewels[i]]  = 1
            
        for j in range(len(stones)):
            if stones[j] in my_dict:
                count += 1
                
        return count
    
A = Solution()
print(A.numJewelsInStones('aw', 'awesome'))
print(A.numJewelsInStones('', 'zero'))
print(A.numJewelsInStones('hi', 'Hello'))
print(A.numJewelsInStones('zz', 'ZZZzZZZ'))
print(A.numJewelsInStones('1', '1one1one1'))