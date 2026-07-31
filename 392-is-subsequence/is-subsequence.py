class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l=0
        r=0
        while l<len(t) and r<len(s):
            if s[r]==t[l]:
                l+=1
                r+=1
            elif s[r]!=t[l]:
                l+=1
        return r==len(s)