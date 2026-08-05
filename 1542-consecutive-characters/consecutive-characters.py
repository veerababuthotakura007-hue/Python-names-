class Solution:
    def maxPower(self, s: str) -> int:
        c=1
        mx_count=1
        for i in range(1,len(s)):
            if s[i-1]==s[i]:
                c+=1
            else:
                mx_count=max(mx_count,c)
                c=1
        return max(mx_count,c)
