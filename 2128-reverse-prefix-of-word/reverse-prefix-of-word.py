class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        k=word.find(ch)
        if k!=-1:
            return word[:k+1][::-1]+word[k+1:]
        return word