class Solution:
    def reverseVowels(self, s: str) -> str:
        string = list(s)
        vowels = 'aeiou'
        j = len(string) - 1
        i = 0
        while i < j:
            if string[i].lower() not in vowels:
                i += 1
            elif string[j].lower() not in vowels:
                j -= 1
            else:
                string[i], string[j] = string[j], string[i]
                i += 1
                j -= 1
        return ''.join(string)   
    
    
A = Solution()   

print(A.reverseVowels("helloworld"))
print(A.reverseVowels("eeeeiiii"))
print(A.reverseVowels(""))
print(A.reverseVowels("reversevowels"))