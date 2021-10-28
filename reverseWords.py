class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(' ')
        rev_words = []
        
        for i in range(len(words)-1, -1, -1):
            if words[i] != '':
                rev_words.append(words[i])  
        return ' '.join(rev_words)