class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        mx=0
        d=set()
        for r in range(len(s)):
            while s[r] in d:
                d.remove(s[l])
                l+=1
            d.add(s[r])
            mx=max(mx,r-l+1)
        return mx 