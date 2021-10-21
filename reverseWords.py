class Solution:
    def reverseWords(self, s: str) -> str:
        revWords = []
        words = s.split(' ')
        striped_words = [word for word in words if word.strip()]
        # print(striped_words)
        if len(striped_words) == 1:
            return ''.join(striped_words)
        for i in range(len(striped_words)-1, -1,-1):
            revWords.append(striped_words[i])
        return " ".join(striped_words)