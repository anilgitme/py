class Solution:
    def reverseString(self, s: List[str]) -> None:   
        i = 0
        j = len(s) -1
        
        while i <= j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        return s
        
        
A = Solution() 
print(A.reverseString(["h","e","l","l","o"]))
print(A.reverseString([""]))
print(A.reverseString(["s"]))
print(A.reverseString(["s","s","s"]))


# 2


class Solution:
    def reverseString(self, s: List[str]) -> None:
        j = len(s) - 1
        if not s:
            return s
        
        for i in range(len(s)):
            if i >= j:
                break
            s[i], s[j] = s[j], s[i]
            j -= 1
        return s


obj = Solution()
print(obj.reverseString(["h","e","l","l","o"]))
print(obj.reverseString([]))
print(obj.reverseString(["R","o","t","o","r"]))
print(obj.reverseString(["z"]))
print(obj.reverseString(["E","e"]))