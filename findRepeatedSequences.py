        
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        dnaDict = {}
        result = []
        for i in range(len(s)-9):
            substring = s[i:i+10]
            # print(substring)
            if substring not in dnaDict:
                dnaDict[substring] = 1
            else:
                dnaDict[substring] += 1  
        for key, value in dnaDict.items():
            if value > 1:
                result.append(key)
        return result